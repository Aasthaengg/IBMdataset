def iinput():
    return [int(i) for i in input().split()]


n, d = iinput()
ans = 0
for _ in range(n):
    p, q = iinput()
    if p**2 + q**2 <= d ** 2:
        ans += 1
print(ans)
