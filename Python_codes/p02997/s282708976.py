N, K = map(int, input().split())

if K > (N - 2) * (N - 1) // 2:
    print(-1)
    exit()

add = (N - 2) * (N - 1) // 2 - K

print(N - 1 + add)
for i in range(2, N + 1):
    print(1, i)

for i in range(2, N):
    for j in range(i + 1, N + 1):
        if add:
            print(i, j)
            add -= 1