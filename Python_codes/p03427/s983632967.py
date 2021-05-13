dd = list(map(int, open(0).read().rstrip()))
n = len(dd)

ans = sum(dd)
tmp = 0

for i in range(n):
    if dd[i] > 0:
        tmp += dd[i]
        ans = max(ans, tmp - 1 + (n-i-1)*9)

print(ans)