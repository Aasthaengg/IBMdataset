import sys
input = sys.stdin.readline

N = int(input())
TA = []

for _ in range(N):
    TA.append([int(x) for x in input().split()])

x, y = TA[0]

for i in range(1, N):
    X, Y = TA[i]
    if X < x or Y < y:
        mul = max(x // X + (x % X != 0), y // Y + (y % Y != 0))
        x, y = X * mul, Y * mul
    else:
        x, y = X, Y
    # print(x, y)

print(x + y)


