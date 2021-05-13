n, k = map(int, input().split())
tds = [list(map(int, input().split())) for _ in range(n)]

tds.sort(key=lambda x:x[1])

arr = {}
for idx, td in enumerate(tds):
    t, d = td
    arr[t] = [d, n - idx - 1]

tds = [y for x, y in tds[::-1]]

base = 0
rest = sum(tds[:k])
res = 0
kind = 0
new_arr = sorted(arr.values(), reverse=True)

for x, y in new_arr:
    kind += 1
    base += x
    if y < k:
        rest -= x
        tds[y] = 0
    else:
        while k >= 1 and tds[k - 1] == 0:
            k -= 1
        rest -= tds[k - 1]
        k -= 1
        if k <= 0:
            break
    res = max(res, kind ** 2 + base + rest)

if k >= 0:
    res = max(res, kind ** 2 + base + rest)

print(res)
