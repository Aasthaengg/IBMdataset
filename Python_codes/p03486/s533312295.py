s = str(input())
t = str(input())
s_dic = {}
for i in range(len(s)):
    s_dic.setdefault(s[i],0)
    s_dic[s[i]] += 1
sort_s = sorted(s_dic.items())
#print(sort_s)
t_dic = {}
for i in range(len(t)):
    t_dic.setdefault(t[i],0)
    t_dic[t[i]] += 1
sort_t = sorted(t_dic.items())
#print(sort_t)
mk_s = ''
for i in range(len(sort_s)):
    for j in range(sort_s[i][1]):
        mk_s += sort_s[i][0]
#print(mk_s)
mk_t = ''
for i in range(len(sort_t)):
    for j in range(sort_t[-(i+1)][1]):
        mk_t += sort_t[-(i+1)][0]
#print(mk_t)

if mk_s<mk_t:
    print('Yes')
else:
    print('No')