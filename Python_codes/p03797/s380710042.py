N, M = map(int, input().split())
d = M - N * 2
print(N + d // 4 if d > 0 else M // 2)