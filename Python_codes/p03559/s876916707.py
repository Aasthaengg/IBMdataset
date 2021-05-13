n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a.sort()
c.sort()
ans = 0
for j in range(n):
    l = 0
    r = n - 1
    i = (l + r) // 2
    while l <= r:
        if a[i] >= b[j]:
            r = i - 1
        else:
            l = i + 1
        i = (l + r) // 2
    l = 0
    r = n - 1
    k = (l + r) // 2
    while l <= r:
        if c[k] <= b[j]:
            l = k + 1
        else:
            r = k - 1
        k = (l + r) // 2
    ans += (i + 1) * (n - (k + 1))
print(ans)