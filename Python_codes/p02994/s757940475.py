n, l = map(int, input().split())
t = list(map(lambda x: l + x, range(n)))
r = sum(t)
dif = 10 ** 100
for i in range(n):
    tmp = sum(t[:i] + t[i + 1:])
    dif_t = abs(r - tmp)
    if dif_t < dif:
        ans = tmp
        dif = dif_t
print(ans)
