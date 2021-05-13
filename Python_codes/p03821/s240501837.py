N = int(input())
a, b = [], []

for i in range(N):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)

total = 0
for i, j in zip(a[::-1], b[::-1]):
    k = i + total
    if k % j != 0:
        total += int((k / j) + 1)*j - k
print(total)
