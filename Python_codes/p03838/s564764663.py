x, y = map(int, input().split())

cnt = 0
if abs(x) < abs(y):
    if x < 0:
        x *= -1
        cnt += 1
    cnt += abs(y) - abs(x)
    x += abs(y) - abs(x)
    if x != y:
        cnt += 1
elif abs(x) == abs(y):
    cnt += 1
else:
    if x > y:
        x *= -1
        cnt += 1
    cnt += abs(x) - abs(y)
    x += abs(x) - abs(y)
    if x != y:
        cnt += 1
print(cnt)
