n = int(input())
a = list(map(int, input().split()))
a.sort()
t = 0
s = 0
for i in range(n-1):
    s += a[i]
    if 2 * s < a[i + 1]:
        t = i + 1

print(n-t)
