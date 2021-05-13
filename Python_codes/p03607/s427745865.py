n = int(input())

ad = dict()
for _ in range(n):
    a = int(input())
    ad.setdefault(a, -1)
    ad[a] *= -1

ans = 0
for c in ad.values():
    if c > 0:
        ans += c
print(ans)

