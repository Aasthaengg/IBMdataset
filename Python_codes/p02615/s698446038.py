n = int(input())
a = list(map(int, input().split()))

a.sort()
a.reverse()
t = n - 1
ans = 0
for i in range(n):
    lim = 2
    if i == 0:
        lim = 1
    for j in range(lim):
        if t > 0:
            ans += a[i]
            t -= 1
print(ans)