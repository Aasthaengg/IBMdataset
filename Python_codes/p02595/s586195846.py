import math

N, D = map(int, input().split())
cnt = 0

for n in range(N):
    X, Y = map(int, input().split())
    check = math.sqrt(X**2 + Y**2)
    if check <= D:
        cnt += 1

print(cnt)