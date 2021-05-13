n, *a = map(int, open(0).read().split())

# hantei
ok = True
for i in range(n - 1):
    if a[i + 1] - a[i] > 1:
        ok = False
if not ok or a[0] != 0:
    print(-1)
    exit()


ans = 0
a = list(reversed(a))
i = 0
while i < n:
    ans += a[i]
    while i < n - 1 and a[i] - 1 == a[i + 1]:
        i += 1
    i += 1
print(ans)
