K = int(input())
A = list(map(int,input().split()))

high = 10**18
low = 0

while high-low > 1:
    mid = (high+low)//2
    tmp = mid
    for i in range(K):
        tmp = tmp//A[i]*A[i]
    if tmp <= 2:
        low = mid
    else:
        high = mid
    L = low
    
high = 10**18
low = 0

while high-low > 1:
    mid = (high+low)//2
    tmp = mid
    for i in range(K):
        tmp = tmp//A[i]*A[i]
    if tmp >= 2:
        high = mid
    else:
        low = mid
    S = high

if S <= L:
    print(S,L)
else:
    print(-1)