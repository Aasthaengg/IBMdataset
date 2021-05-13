a, v = map(int, input().split())
b, w = map(int, input().split())

t = int(input())

if a == b:
    print('YES')
    exit()

if w >= v:
    print('NO')
    exit()

d = abs(a - b)

vel = v - w

if (d + vel - 1) // vel > t:
    print('NO')
else:
    print('YES')
