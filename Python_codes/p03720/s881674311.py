N,M = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(M)]

g = {i:0 for i in range(N)}

for a,b in ab:
    g[a-1] += 1
    g[b-1] += 1
    
for i in g.values():
    print(i)