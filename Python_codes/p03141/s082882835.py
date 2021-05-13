n = int(input())
ab = [(ai, bi) for ai, bi in (map(int, input().split())  for _ in range(n))]

ab.sort(key=lambda p: - p[0] - p[1])
print(sum(p[0] for p in ab[::2]) - sum(p[1] for p in ab[1::2]))
