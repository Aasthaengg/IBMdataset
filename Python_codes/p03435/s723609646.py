import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

c = [[int(x) for x in input().split()] for _ in range(3)]

flag = 1

for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            if c[0][0] - a1 == c[1][0] - a2 and c[1][0] - a2 == c[2][0] - a3:
                if c[0][1] - a1 == c[1][1] - a2 and c[1][1] - a2 == c[2][1] - a3:
                    if c[0][2] - a1 == c[1][2] - a2 and c[1][2] - a2 == c[2][2] - a3:
                        flag = 0

if flag:
    print('No')
else:
    print('Yes')

