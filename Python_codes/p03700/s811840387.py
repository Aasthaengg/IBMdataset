import math
N,A,B = map(int,input().split())
H = [int(input()) for _ in range(N)]
d = A-B
high = 10**9
low = 0
while high-low>1:
    mid = (high+low)//2
    D = []
    for i in range(N):
        if H[i]-mid*B>0:
            D.append(H[i]-mid*B)
    cnt = 0
    for h in D:
        cnt += math.ceil(h/d)
    if cnt<=mid:
        high = mid
    else:
        low = mid
print(high)