S = input()

str_list = list('abcdefghijklmnopqrstuvwxyz')
str_cnt = [0 for i in range(len(str_list))]

for i in range(len(S)):
    s = S[i]
    
    index_s = str_list.index(s)
    str_cnt[index_s] += 1

if (0 not in str_cnt):
    ans = 'None'
else:
    ans = str_list[str_cnt.index(0)]

print(ans)
