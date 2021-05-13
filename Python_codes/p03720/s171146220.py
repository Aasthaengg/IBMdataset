N, M = map(int, input().split())
R = [0 for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    R[a-1] += 1
    R[b-1] += 1
for r in R:
    print(r)
