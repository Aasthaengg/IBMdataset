n, t = map(int, input().split(" "))

a = map(int, input().split(" "))

INF = 1000000000000

max_price = -1
min_price = -1

min_pos = 1
max_pos = 1
max_diff = 0
tmp = INF
ans = 0

for c in a:
    if max_price < 0 or min_price < 0:
        max_price = c
        min_price = c
        continue

    if max_price == c:
        max_pos += 1
        tmp = min(tmp, min_pos, max_pos)

    if min_price == c:
        min_pos += 1

    if max_price < c:
        max_price = c
        max_pos = 1

        if max_diff == max_price - min_price:
            tmp = min(tmp, min_pos, max_pos)

        elif max_diff < max_price - min_price:
            max_diff = max_price - min_price
            ans = 0
            tmp = min(tmp, min_pos, max_pos)

    if min_price > c:
        min_price = c
        max_price = c
        min_pos = 1
        ans += (tmp if tmp < INF else 0)
        tmp = INF

if tmp < INF:
    ans += tmp

print(ans)
