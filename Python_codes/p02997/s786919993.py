from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]

if K > ((N - 1) * (N - 2)) // 2:
    print(-1)
    exit()

ans = []
for i in range(2, N + 1):
    ans.append((1, i))

E = ((N - 1) * (N - 2)) // 2 - K

for j in range(2, N + 1):
    if E == 0:
        break
    for k in range(j + 1, N + 1):
        ans.append((j, k))
        E -= 1
        if E == 0:
            break

print(N - 1 + ((N - 1) * (N - 2)) // 2 - K)
for a in ans:
    print(*a)
