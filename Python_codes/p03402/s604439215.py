import sys
input = sys.stdin.readline

a, b = [int(x) for x in input().split()]

white = [['.'] * 100 for _ in range(50)]
black = [['#'] * 100 for _ in range(50)]

a, b = a - 1, b - 1

if b != 0:
    for i in range(0, 50, 2):
        flag = 0
        for j in range(0, 100, 2):
            white[i][j] = '#'
            b -= 1
            if b == 0:
                flag = 1
                break
        if flag:
            break

if a != 0:
    for i in range(1, 50, 2):
        flag = 0
        for j in range(1, 100, 2):
            black[i][j] = '.'
            a -= 1
            if a == 0:
                flag = 1
                break
        if flag:
            break
print(100, 100)
for i in white:
    print(''.join(i))
for j in black:
    print(''.join(j))



