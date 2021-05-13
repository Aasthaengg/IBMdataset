X, Y = map(int, input().split())
cnt = 1
while True:
    X = 2 * X
    if X <= Y:
        cnt += 1
    else:
        break
print(cnt)
