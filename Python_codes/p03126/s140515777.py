N, M = map(int, input().split())
K_A = [list(map(int, input().split())) for _ in range(N)]
candidate = {i for i in range(1, M + 1)}
for line in K_A:
    candidate = candidate & set(line[1:])
print(len(candidate))
