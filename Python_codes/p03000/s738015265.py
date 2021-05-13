read = lambda: list(map(int, input().split()))
n, x = read()
l = read()
s = 0
ans = 1
for ind, d in enumerate(l):
    s += d
    if s > x:
        break
    ans += 1
print(ans)