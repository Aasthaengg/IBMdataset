# ソートしてカウント
# (2以上の場合、)個数のn*(n-1)/2

n = int(input())
d = dict()
for i in range(n):
    s = list(input())
    s.sort()
    sl = ''.join(s)
    if d.get(sl) == None:
        d[sl] = 1
    else:
        d[sl] = d[sl] + 1

ans = 0
for k in d.keys():
    ans = ans + d[k] * (d[k] - 1) // 2

print(ans)
