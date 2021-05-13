import bisect
from collections import OrderedDict
def resolve():
    N, C = list(map(int, input().split()))
    P = []
    cal = [0]
    for i in range(N):
        x, v = list(map(int, input().split()))
        P.append(x)
        cal.append(cal[i]+v)
    
    to_right = [0]
    for i in range(N):
        to_right.append(max(to_right[i], cal[i+1]-P[i]))
    to_left = [0]
    for i in range(N):
        to_left.append(max(to_left[i], cal[N]-cal[N-i-1]-(C-P[-i-1])))
    right_left = 0
    for i in range(N-1):
        right_left = max(right_left, cal[i+1]+to_left[N-i-1]-2*P[i])
    left_right = 0
    for i in range(N-1):
        left_right = max(left_right, cal[N]-cal[N-i-1]+to_right[N-i-1]-2*(C-P[-i-1]))
    print(max(to_right+to_left+[right_left, left_right]))

    
if '__main__' == __name__:
    resolve()
