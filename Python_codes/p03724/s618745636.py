N,M = map(int,input().split())

G = [[] for i in range(N)]

for i in range(M) :
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

for i in range(N) :
    if len(G[i]) % 2 != 0 :
        ans = "NO"
        break
else :
    ans = "YES"

print(ans)
