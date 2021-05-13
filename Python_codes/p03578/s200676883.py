N = int(input())
D_list = list(map(int, input().split()))
M = int(input())
T_list = list(map(int, input().split()))

dic_T = {}
for i in T_list:
    if i in dic_T:
        dic_T[i] += 1
    else:
        dic_T[i] = 1

dic_D = {}
for i in D_list:
    if i in dic_D:
        dic_D[i] += 1
    else:
        dic_D[i] = 1

for i in dic_T:
    if i in dic_D:
        if not dic_T[i] <= dic_D[i]:
            print('NO')
            exit()
    else:
        print('NO')
        exit()

print('YES')

