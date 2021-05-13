n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 1:
        m = i
        break
l = [m - k + 1, m]
ans = 114514
for i in range(k):
    x = l[0] + i
    y = l[1] + i
    if not x < 0 and not y >= n:
        c = 1
        while True:
            if x <= 0:
                break
            x -= k - 1
            c += 1
        while True:
            if y >= n - 1:
                break
            y += k - 1
            c += 1
        if c < ans:
            ans = c
print(ans)