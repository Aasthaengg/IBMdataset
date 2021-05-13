n,t = map(int,input().split())
A = list(map(int,input().split()))
m = 10**9+1 
M = -1
ans = 1
for i in range(n):
    x = A[i]
    m = min(x,m)
    p = x-m
    if p > M:
        ans = 1
        M = p
    elif p == M:
        ans += 1
if M <= 0:
    ans = 0
print(ans)