n, m = list(map(int, input().split()))

ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort()

p = 0
x = 0

for i in range(n):
    if x + ab[i][1] < m:
        x += ab[i][1]
        p += ab[i][0] * ab[i][1]
    else:
        p += ab[i][0] * (m - x)
        break

print(p)