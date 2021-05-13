n, k = map(int, input().split())
total = 0
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()
for a, b in ab:
    total += b
    if total >= k:
        print(a)
        break