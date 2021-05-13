N, M = map(int, input().split())
D = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    D[a - 1] += 1
    D[b - 1] += 1

print(*D, sep='\n')