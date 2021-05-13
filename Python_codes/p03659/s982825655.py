n = int(input())
a = list(map(int, input().split()))


left = a[0]
right = sum(a[1:])
ans = abs(left - right)
for i in range(1, n-1):
    left += a[i]
    right -= a[i]
    ans = min(ans, abs(left-right))
print(ans)
