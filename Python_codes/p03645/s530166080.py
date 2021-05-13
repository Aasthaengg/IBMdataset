n,m=map(int,input().split())
adj=[[]for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    adj[a].append(b)
    adj[b].append(a)
for i in adj[0]:
    if n-1 in adj[i]:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")