n, m = map(int, input().split())
M = [map(int, input().split()) for _ in range(n)]
V = [int(input()) for _ in range(m)]
for r in M:
    print(sum(x*y for x, y in zip(r, V)))