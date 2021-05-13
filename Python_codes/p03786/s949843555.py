n = int(input())
a = list(map(int, input().split()))
a.sort()
c = 1
m = 0
for i in range(n - 1):
    m += a[i]
    if 2 * m >= a[i + 1]:
        c += 1
    else:
        c = 1
print(c)