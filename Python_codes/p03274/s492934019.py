n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = []
for i in range(n - k + 1):
    left = x[i]
    right = x[i + k - 1]
    if abs(left) > abs(right):
        ans.append(abs(right) + abs(left - right))
    else:
        ans.append(abs(left) + abs(right - left))

print(min(ans))