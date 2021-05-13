n, h = map(int, input().split())
a = []
b = []
for _ in range(n):
    tmp_a, tmp_b = map(int, input().split())
    a.append(tmp_a)
    b.append(tmp_b)

v = max(a)
b.sort(reverse=True)
i = 0
while i < n and b[i] > v and h > 0:
    h -= b[i]
    i += 1

if h <= 0:
    print(i)
else:
    print(i + (h + v - 1) // v)