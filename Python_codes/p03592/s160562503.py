n, m, k = map(int, input().split())
s = set()
for i in range(n + 1):
    s.add(i * m)
for i in range(m + 1):
    s.add(i * n)
for i in range(1, n):
    for j in range(1, m):
        s.add(i * j + (n - i) * (m - j))
if k in s:
    print("Yes")
else:
    print("No")