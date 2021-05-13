N,M = map(int,input().split())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[0])
cnt = 0
cost = 0
for i in range(N):
    a,b = A[i]
    if cnt+b<=M:
        cnt += b
        cost += a*b
    else:
        d = M-cnt
        cost += a*d
        break
print(cost)