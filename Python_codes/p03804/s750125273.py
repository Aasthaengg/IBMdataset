n, m = [int(s) for s in input().split()]
a_list = [input() for _ in range(n)]
b_list = [input() for _ in range(m)]
stop = n - m + 1
for i in range(stop):
    for j in range(stop):
        break_flag = False
        for x in range(m):
            for y in range(m):
                if a_list[i + x][j + y] != b_list[x][y]:
                    break_flag = True
                    break
            if break_flag:
                break
        else:
            print("Yes")
            exit()
print("No")