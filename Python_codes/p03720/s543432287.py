N,M = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(M)]

g = {i:[] for i in range(N)}

for a,b in ab:
    g[a-1].append(b)
    g[b-1].append(a)
    
for i in g.values():
    print(len(i))