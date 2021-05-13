n,m = map(int,input().split())
V = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    V[a].append(b)
    V[b].append(a)
W = V[1]
z = []
for x in W:
    z.append(V[x])
s = 0
for q in z:
    if n in q:
        s = 1
        break
if s == 1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")