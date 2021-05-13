n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] <= b[i]:
        ans += a[i]
        b[i] -= a[i]
        a[i] = 0
    else:
        ans += b[i]
        a[i] -= b[i]
        b[i] = 0
    if b[i] > 0:
        tmp = max(0, a[i + 1] - b[i])
        if tmp == 0:
            ans += a[i + 1]
        else:
            ans += b[i]
        a[i + 1] = tmp
print(ans)