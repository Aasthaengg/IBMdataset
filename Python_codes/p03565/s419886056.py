s = input()
t = input()

s_num = len(s)
t_num = len(t)

ans_list = []
ind_list = []

if s_num<t_num:
    ans_list.append('UNRESTORABLE')
else:
    for i in range(s_num -t_num + 1):
        flg = True
        for j in range(t_num):
            if s[i+j] == '?':
                pass
            elif s[i+j]==t[j]:
                pass
            else:
                flg=False
                break
        if flg:
            ind_list.append(i)
if len(ind_list) ==0:
    ans_list.append('UNRESTORABLE')
else:
    for i in ind_list:
        ans = ''
        j=0
        while j <s_num:
            if j==i:
               ans = ans+t
               j = j + t_num
            elif s[j] == '?':
                ans = ans + 'a'
                j = j + 1
            else:
                ans = ans + s[j]
                j = j + 1
        ans_list.append(ans)

print(min(ans_list))