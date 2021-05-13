from bisect import bisect_left

n, m = map(int, input().split())

div = []
i = 1
while i * i <= m:
    if m % i == 0:
        div.append(i)
        div.append(m // i)
    i += 1

div.sort()

print(m // div[bisect_left(div, n)])