N, M = map(int, input().split())
shops = []
for _ in range(N):
    a, b = map(int, input().split())
    shops.append((a, b))
shops = sorted(shops, key=lambda s: s[0])
m = 0
total = 0
for a, b in shops:
    if m + b >= M:
        total += (M - m) * a
        break
    else:
        total += a * b
        m += b
print(total)
