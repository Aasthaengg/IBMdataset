n, h, w = map(int, input().split())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    if (a >= h) & (b >= w):
        ans += 1
print(ans)