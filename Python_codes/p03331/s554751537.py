n = int(input())
ans = 10 ** 5
for a in range(1, n):
    ak = sum([int(a) for a in str(a)])
    bk = sum([int(b) for b in str(n - a)])
    if ans > ak + bk:
        ans = ak + bk
print(ans)