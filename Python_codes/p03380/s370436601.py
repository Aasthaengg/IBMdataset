
n = int(input())
a = list(map(int, input().split()))
x = max(a)
a.sort()
min = 10 ** 10
del a[-1]
for i in range(n - 1):
    if min > abs(x / 2 - a[i]):
        min = abs(x / 2 - a[i])
        y = a[i]
print(x, y)