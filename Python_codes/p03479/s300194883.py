X, Y = map(int, input().split())
ans = 1
nextX = X
for i in range(0, 10 ** 8):
    t = nextX * 2
    if t <= Y:
        ans += 1
        nextX = t
    else:
        break
print(ans)
