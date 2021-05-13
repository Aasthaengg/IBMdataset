x, n = map(int, input().split())
p = list(map(int, input().split()))

dmin = 10 ** 9
ans = 0

for i in range(0, 102):
    if i not in p:
        d = (x - i) * (x - i)
        if d < dmin:
            dmin = d
            ans = i

print(ans)