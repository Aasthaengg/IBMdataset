n, k = map(int, input().split())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
ab.sort(key=lambda x: x[0])

for a, b in ab:
    k -= b
    if k <= 0:
        ans = a
        break
print(ans)
