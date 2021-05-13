N = int(input())
prev_t, prev_x, prev_y = 0, 0, 0
ans = "Yes"
for _ in range(N):
    t, x, y = map(int, input().split())
    if t - prev_t < abs(prev_x - x) + abs(prev_y - y):
        ans = "No"
    if (abs(prev_x - x) + abs(prev_y - y)) % 2 != (t - prev_t) % 2:
        ans = "No"
    prev_t, prev_x, prev_y = t, x, y
print(ans)