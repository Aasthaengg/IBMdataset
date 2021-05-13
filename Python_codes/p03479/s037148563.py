X, Y = map(int, input().split())

cnt = 1
k = X
while k * 2 <= Y:
    cnt += 1
    k *= 2

print(cnt)
