N = int(input())
a = list(map(int, input().split()))

s = sum(a)
x = a[0]
res = abs(s - 2 * x)
for i in range(1, N - 1):
    x += a[i]
    y = s - x
    if res > abs(y - x):
        res = abs(y - x)
print(res)
