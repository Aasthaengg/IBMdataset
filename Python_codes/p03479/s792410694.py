X, Y = map(int, input().split())
cnt = 1
while True:
    X *= 2
    if X > Y:
        break
    cnt += 1
print(cnt)