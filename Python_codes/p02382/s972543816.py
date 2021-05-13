import math
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for p in range(1, 4):
    D = []
    for count in range(n):
        D.append((math.fabs(A[count] - B[count]))**p)
    if p==1:
        di = max(D)
    d=(sum(D))**(1/p)
    print('%.06f' % d)
print('%.06f' % di)