# -*- coding: utf-8 -*-
N = int(input())

matrix = [list(map(int, input().split(' '))) for _ in range(N)]
buf = [list(m) for m in matrix]

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            buf[i][j] = min(buf[i][j],  buf[i][k] + buf[k][j])

for i in range(N):
    for j in range(N):
        if buf[i][j] != matrix[i][j]:
            print(-1)
            exit()

is_used = [[True for _ in range(N)] for m in matrix]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if k != i and k != j:
                if matrix[i][k] + matrix[k][j] == matrix[i][j]:
                    is_used[i][j] = False

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if is_used[i][j]:
            ans += matrix[i][j]

# ans = (sum([sum(b) for b in matrix]) - diff) // 2
print(ans)

