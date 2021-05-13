#coding:utf-8
n, t_u = map(int,input().split())
name_pro_dict = {}
for i in range(n):
    name, pro = input().split()
    name_pro_dict[name] = int(pro)

t = 0
while name_pro_dict:
    keys = list(name_pro_dict.keys())
    for key in keys:
        if name_pro_dict[key] <= t_u:
            t += name_pro_dict[key]
            print(key, t)
            del name_pro_dict[key]
        else:
            name_pro_dict[key] -= t_u
            t += t_u
            
