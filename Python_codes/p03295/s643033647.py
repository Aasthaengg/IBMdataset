N,M = map(int,input().split())
lis = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    lis[a].append(i+1)
    lis[b].append(-(i+1))
for i in range(N):
    lis[i].sort()

ans = 0
d = set()
for i in range(N):
    for j in range(len(lis[i])):
        if lis[i][j] < 0:
            if -lis[i][j] in d:
                d = set()
                ans += 1
        else:
            d.add(lis[i][j])
print(ans)
