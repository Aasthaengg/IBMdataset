n, k = map(int, input().split())
data = list(map(int, input().split()))
l = 0
r = k - 1
ans = float("inf")
while True:
    if r == n:
        break
    ans = min(ans, abs(data[l]) + abs(data[l] - data[r]), abs(data[r]) + abs(data[r] - data[l]))
    l += 1
    r += 1
print(ans)
