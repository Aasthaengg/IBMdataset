D = int(input())

last_list = [0 for i in range(27)]
c_list = list(map(int, input().split()))
c_list = [""] + c_list
# print(c_list)
S_list = [[]for i in range(D)]
P_list = [0 for i in range(27)]
for i in range(D):
    S_list[i] = list(map(int, input().split()))
    S_list[i] = [""] + S_list[i]
S_list = [""] + S_list
# print(S_list)

for i in range(1,D+1):
    S = 0
    t = int(input())
    for j in range(1,27):
        if j == t:
            P_list[j] += S_list[i][j]
            last_list[j] = i
            # print(S_list[i][j])
        else:
            P_list[j] -= c_list[j] * (i-last_list[j])
    for i in range(1,27):
        S += P_list[i]
    print(S)





# t_list = []
# for i in range(D):
#     t_list.append(int(input()))
