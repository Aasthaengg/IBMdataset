INF = 1 << 60
n = int(input())
ans = INF
for a in range(1, n):
    b = str(n - a)
    a = str(a)
    total_a = 0
    total_b = 0
    for i in a:
        total_a += int(i)
    for i in b:
        total_b += int(i)
    ans = min(ans, total_a + total_b)
print(ans) 