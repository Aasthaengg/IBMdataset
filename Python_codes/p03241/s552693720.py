n, m = map(int, input(). split())
b = set()
i = 1
while i * i <= m:
    if m % i == 0:
        b.add(i)
        b.add(m // i)
    i += 1
ans = 1
for i in b:
    if i * n <= m:
        ans = max(ans, i)
print(ans)
