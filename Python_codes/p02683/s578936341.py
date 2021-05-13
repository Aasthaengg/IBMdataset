N,M,X = map(int, input().split())
books = [[] for _ in range(N)]
for i in range(N):
    books[i] = list(map(int, input().split()))
Inf = int(1e20)
ans = Inf
for i in range(2**N):
    a = [0 for _ in range(M+1)]
    for j in range(N):
        if (i & (1 << j)):
            a = [x+y for (x,y) in zip(a,books[j])]
    ok = True
    for k in range(M):
        if a[k+1] < X:
            ok = False
    if not ok:
        continue
    ans = min(ans, a[0])
if ans == Inf:
    ans = -1
print(ans)
