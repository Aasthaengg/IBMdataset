n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = []
for i in range(n - k + 1):
    left = x[i]
    right = x[i + k - 1]
    ans.append(min(abs(left) + abs(right - left),
                   abs(right) + abs(left - right)))

print(min(ans))