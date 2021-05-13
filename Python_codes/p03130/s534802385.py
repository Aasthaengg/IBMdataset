G = {i:[] for i in range(1,5)}
for _ in range(3):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
cnt = 0
for x in G:
    if len(G[x])%2==1:
        cnt += 1
if cnt>2:
    print("NO")
else:
    print("YES")