n = int(input())
a = list(map(int, input().split()))

ans = [0] * n

sign = True
for i in range(n):
    if sign:
        ans[0] += a[i]
    else:
        ans[0] -= a[i]
    sign = not sign

for i in range(1, n):
    ans[i] = 2 * a[i-1] - ans[i-1]

print(*ans, sep=' ')