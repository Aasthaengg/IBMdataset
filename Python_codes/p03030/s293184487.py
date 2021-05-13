N = int(input())
rev = {}
ind_dic = {}
for i in range(1, N+1):
    k, v = input().split()
    
    if k in rev:
        rev[k].append(v)
    else:
        rev[k] = [v]
    ind_dic[v] = i

for v in rev.values():
    for i in range(len(v)):
        v[i] = int(v[i])
    v.sort(reverse=True)

key_lst = []
for k in rev.keys():
    key_lst.append(k)
key_lst.sort()

new_dic = {}
for k in key_lst:
    new_dic[k] = rev[k]

for k in new_dic.keys():
    for i in range(len(new_dic[k])):
        print(ind_dic[str(new_dic[k][i])])