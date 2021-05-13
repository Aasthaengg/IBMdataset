n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, n - 1):
    a, b, c = arr[i - 1], arr[i], arr[i + 1]
    if a < b < c or a > b > c:
        ans += 1

print(ans)