c = [list(map(int, input().split())) for _ in range(3)]
a1 = c[0][0]
for i in range(a1+1):
    b1 = a1 - i
    b2 = c[0][1] - i
    b3 = c[0][2] - i
    a2 = c[1][0] - b1
    a3 = c[2][0] - b1

    if a2+b2 ==c[1][1] and a2+b3==c[1][2] and a3+b2 == c[2][1] and a3+b3 == c[2][2]:
        print('Yes')
    else:
        print('No')
    exit()