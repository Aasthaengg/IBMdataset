# https://atcoder.jp/contests/abc047/tasks/abc047_b

w, h, n = [int(i) for i in input().split()]

left = 0
right = w
bottom = 0
top = h

for _ in range(n):
    x, y, a = [int(i) for i in input().split()]
    if a == 1:
        left = max(left, x)
    elif a == 2:
        right = min(right, x)
    elif a == 3:
        bottom = max(bottom, y)
    elif a == 4:
        top = min(top, y)

if top <= bottom or right <= left:
    print(0)
else:
    print((right - left) * (top - bottom))
