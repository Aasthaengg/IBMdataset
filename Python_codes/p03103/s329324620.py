N,M = map(int,input().split())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[0])
ans = 0
tot = 0
for i in range(N):
    a,b = A[i]
    if tot+b<M:
        tot += b
        ans += a*b
    else:
        n = M-tot
        ans += a*n
        break
print(ans)