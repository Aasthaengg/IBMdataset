N = int(input())
al = [[] for _ in range(N+1)]
for i in range(1,N+1):
    al[i] = int(input())
#print(al)

#初期値
n = 1
cnt = 1
visited = [0 for _ in range(N+1)]
visited[1] = 1
while al[n] != 2:
    cnt += 1
    n = al[n]
    if visited[n] == 1:
        print(-1)
        exit()
    else:
        visited[n] = 1
print(cnt)


