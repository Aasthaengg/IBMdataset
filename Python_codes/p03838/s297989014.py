X, Y = map(int, input().split())

res = 10**10

if abs(X) == abs(Y):
    res = 1

if abs(X) < abs(Y):
    cnt = 0
    if X < 0:
        cnt += 1
    cnt += abs(abs(X)-abs(Y))
    if Y < 0:
        cnt += 1
    res = min(cnt, res)

if abs(X) > abs(Y):
    cnt = 0
    if X > 0:
        cnt += 1
    cnt += abs(abs(X)-abs(Y))
    if Y > 0:
        cnt += 1
    res = min(cnt, res)

print(res)