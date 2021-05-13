S = input()
T = input()

l = len(S)
S_lst = [None] * l
T_lst = [None] * l
S_dic = {}
T_dic = {}

s_cnt = 0
for i, s in enumerate(S):
    if s in S_dic:
        n = S_dic[s]
        S_lst[i] = n
    else:
        S_lst[i] = s_cnt
        S_dic[s] = s_cnt
        s_cnt += 1


t_cnt = 0
for i, t in enumerate(T):
    if t in T_dic:
        n = T_dic[t]
        T_lst[i] = n
    else:
        T_lst[i] = t_cnt
        T_dic[t] = t_cnt
        t_cnt += 1


if s_cnt != t_cnt:
    print('No')
    exit()

for i in range(l):
    if S_lst[i] != T_lst[i]:
        print('No')
        exit()

print('Yes')
