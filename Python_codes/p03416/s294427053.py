a, b = map(int, input().split())
ans = 0
for i in range(a, b+1):
    nor = str(i)
    rev = "".join(list(reversed(nor)))
    if nor == rev:
        ans += 1
print(ans)