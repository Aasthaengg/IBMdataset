
k, s = map(int, input().split())

ans = 0
x_min = max(0, s - k - k) 
x_max = min(k, s)
for x in range(x_min, x_max + 1):
    y_min = max(0, s - x - k)
    y_max = min(k, s - x)
    ans += y_max - y_min + 1
print(ans)
