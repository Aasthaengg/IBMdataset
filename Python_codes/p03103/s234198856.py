N,M = map(int,input().split())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[0])
cnt = 0
cost = 0
i = 0
while i<N:
    a,b = A[i]
    if cnt+b<=M:
        cnt += b
        cost += a*b
    else:break
    i += 1
if cnt<M:
    a,b = A[i]
    cost += (M-cnt)*a
print(cost)