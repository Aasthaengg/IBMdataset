# https://atcoder.jp/contests/agc008/tasks/agc008_a
x, y = map(int, input().split())

ans = float('inf')
for i in range(4):
    t = 0
    if i == 0:
        tx = -1 * x
        ty = y
        t += 1
    elif i == 1:
        tx = x
        ty = -1 * y
        t += 1
    elif i == 2:
        tx = -1 * x
        ty = -1 * y
        t += 2
    else:
        tx = x
        ty = y
    if tx <= ty:
        t += ty - tx
        ans = min(ans, t)

print(ans)