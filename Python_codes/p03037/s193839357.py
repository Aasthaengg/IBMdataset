n, m = map(int, input().split())
imos = [0] * (n + 1)
for _ in range(m):
    l, r = map(int, input().split())
    imos[l-1] += 1
    imos[r] -= 1
cnt = 1 if imos[0] == m else 0
for i in range(1, n):
    imos[i] += imos[i-1]
    if imos[i] == m:
        cnt += 1
print(cnt)
