N = int(input())
s_list = [input() for _ in range(N)]
M = int(input())
t_list = [input() for _ in range(M)]

rev_list = []
for i in range(len(s_list)):
    a = s_list.count(s_list[i])
    b = t_list.count(s_list[i])
    if a >= b:
        ans_num = a-b
    else:
        ans_num = 0
    rev_list.append(ans_num)
    
print(max(rev_list))