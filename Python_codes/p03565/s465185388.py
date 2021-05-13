S_hatena = input()
T_hint = input()

N = len(S_hatena)
ans_list = []

for i in range(N):
    index_init = i
    index_end = i + len(T_hint) - 1
    
    s = S_hatena[index_init:index_end + 1]
    FLAG = True
    
    if (index_end < N):
        for j in range(len(T_hint)):
            if (s[j] != T_hint[j] and s[j] != '?'):
                FLAG = False
                break
    else:
        FLAG = False
    
    if (FLAG):
        tmp_ans = S_hatena[:index_init] + T_hint + S_hatena[index_init + len(T_hint):]
        tmp_ans = tmp_ans.replace('?', 'a')
        ans_list.append(tmp_ans)

ans_list.sort()

if (len(ans_list) > 0):
    print(ans_list[0])

else:
    print('UNRESTORABLE')