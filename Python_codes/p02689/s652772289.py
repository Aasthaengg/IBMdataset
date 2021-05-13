N,M = map(int,input().split())
H = list(map(int,input().split()))
H.insert(0,0)
G = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
cnt = 0
for i in range(1,N+1):
    flag = 1
    for x in G[i]:
        if H[x]>=H[i]:
            flag = 0
            break
    if flag==1:
        cnt += 1
print(cnt)