N,M = map(int,input().split())
res = {}
for i in range(1,N+1):
    res[i] = 0
for _ in range(M):
    a,b = map(int,input().split())
    res[a] += 1
    res[b] += 1
for key in sorted(res.keys()):
    print(res[key])