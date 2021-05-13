n, m = map(int, input().split())
d = []
i = 1
while i ** 2 <= m:
    if m % i == 0:
        d.append(i)
        j = m // i
        if j != i:
            d.append(j)
    i += 1
d.sort(reverse=True)
for t in d:
    if m // t >= n:
        print(t)
        exit()
