n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]

t.sort()

waitP = 1
l = t[0]
ans = 0

for i in range(1, n):
    if waitP == c:
        ans += 1
        l = t[i]
        waitP = 1
        if i == n - 1:
            ans += 1
    elif waitP != c:
        if t[i] - l <= k:
            waitP += 1
            if i == n - 1:
                ans += 1
        elif t[i] - l > k:
            ans += 1
            l = t[i]
            waitP = 1
            if i == n - 1:
                ans += 1

print(ans)