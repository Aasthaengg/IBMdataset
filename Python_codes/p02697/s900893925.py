n, m = map(int, input().split())
i = 0
c = 0
while (i + 1) + i < (n - i - (i + 1)) and c < m:
    print(i + 1, n - i)
    c += 1
    i += 1
a = n // 2 + n % 2
for i in range(m - c):
    print(a - i - 1, a + i + 1)