N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Map = [[] for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(N):
            if A[i][j] != A[j][i]:
                print(-1)
                exit()
            if k == i or k == j:
                continue
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                exit()
            elif A[i][j] == A[i][k] + A[k][j]:
                break
        else:
            Map[i].append(j)
            Map[j].append(i)
            ans += A[i][j]
print(ans)
