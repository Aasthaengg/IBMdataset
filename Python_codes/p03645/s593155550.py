f=lambda:map(int,input().split())
n,m=f()
c=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=f()
    c[a]+=[b]
    c[b]+=[a]
print("IMPOSSIBLE" if all(n not in c[i] for i in c[1]) else "POSSIBLE")