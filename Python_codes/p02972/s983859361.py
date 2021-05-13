n = int(input())
a = [0] + list(map(int, input().split()))

m = 0
b = [0] * (n + 1)

for i in reversed(range(1, n+1)):
    cnt = 0
    for j in range(i, n+1, i):
        cnt += b[j]
    if cnt % 2 != a[i]:
        b[i] = 1
        m += 1

print(m)
if m > 0:
    print(*[i for i, j in enumerate(b) if j == 1], sep=' ')
