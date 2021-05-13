c = [list(map(int, input().split())) for _ in range(3)]

for a1 in range(min(c[0])+1):
    for a2 in range(min(c[1])+1):
        for a3 in range(min(c[2])+1):
            b1 = c[0][0] - a1
            b2 = c[0][1] - a1
            b3 = c[0][2] - a1

            if c[1][0] == a2+b1 and c[1][1] == a2 + b2  and c[1][2] == a2 + b3 and c[2][0] == a3+b1 and c[2][1] == a3 + b2  and c[2][2] == a3 + b3:
                print('Yes')
                exit()
print('No')