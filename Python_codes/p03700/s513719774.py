import math
N,A,B = map(int,input().split())
H = [int(input()) for _ in range(N)]
low = sum(H)//((N-1)*B+A)-1
high = max(H)//B+1
while high-low>1:
    mid = (high+low)//2
    cnt = 0
    for i in range(N):
        cnt += math.ceil(max(H[i]-mid*B,0)/(A-B))
    if cnt<=mid:
        high = mid
    else:
        low = mid
print(high)