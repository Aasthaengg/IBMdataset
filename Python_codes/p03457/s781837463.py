n = int(input())
t_list = [list(map(int, input().split())) for _ in range(n)]

x_dif = t_list[0][1]
y_dif = t_list[0][2]
t_dif = t_list[0][0]
if x_dif + y_dif <= t_dif and (x_dif+y_dif)%2 == t_dif%2:
    pass
else:
    print('No')
    exit()
for i in range(n-1):
    x_dif = abs(t_list[i+1][1]-t_list[i][1])
    y_dif = abs(t_list[i+1][2]-t_list[i][2])
    t_dif = t_list[i+1][0]-t_list[i][0]
    # print(i, x_dif, y_dif, t_dif)
    if x_dif + y_dif <= t_dif and (x_dif+y_dif)%2 == t_dif%2:
        pass
    else:
        print('No')
        exit()
print('Yes')
