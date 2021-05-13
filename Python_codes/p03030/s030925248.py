N = int(input())
S_and_P_and_res_num = [['', 0, 0] for _ in range(N)]
for i in range(N):
    s, p = input().split()
    S_and_P_and_res_num[i][0] = s
    S_and_P_and_res_num[i][1] = int(p)
    S_and_P_and_res_num[i][2] = i + 1
S_and_P_and_res_num.sort(key=lambda x: (x[0], -x[1]))
[print(S_and_P_and_res_num[i][2]) for i in range(N)]
