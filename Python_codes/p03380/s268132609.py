n = int(input())
a = sorted(map(int, input().split()))
m = a[-1]
for i in range(n - 1):
    c = abs(a[i] - a[-1] / 2)
    if c < m:
        m = c
        r = i
print(a[-1], a[r])
