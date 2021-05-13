N, K = map(int, input().split())

if K>N*(N-1)//2-(N-1):
    print(-1)
    exit()

is_ban = [[False]*N for _ in range(N)]

for i in range(1, N):
    for j in range(i+1, N):
        if K==0:
            break
        
        is_ban[i][j] = True
        K -= 1

ans = []

for i in range(N):
    for j in range(i+1, N):
        if not is_ban[i][j]:
            ans.append((i, j))
    
print(len(ans))

for u, v in ans:
    print(u+1, v+1)