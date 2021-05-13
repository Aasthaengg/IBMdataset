l = [list(map(int, input().split())) for _ in range(3)]

for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            b1 = l[0][0] - a1
            b2 = l[0][1] - a1
            b3 = l[0][2] - a1

            a = [a1, a2, a3]
            b = [b1, b2, b3]

            cnt = 0
            for i in range(3):
                for j in range(3):
                    if l[i][j] == a[i] + b[j]:
                        cnt += 1
            if cnt == 9:
                print("Yes")
                exit()
print("No")
