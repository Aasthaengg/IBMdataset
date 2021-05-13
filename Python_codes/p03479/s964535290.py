X, Y = list(map(int, input().split()))

cnt = 1
x = X
while True:
    x = 2 * x
    if x > Y:
        break
    cnt += 1
print(cnt)
