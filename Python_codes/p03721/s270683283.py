N_kai, K_ban = map(int, input().split())

dic = {}

for i in range(N_kai):
    a, b_ko = map(int, input().split())
    
    if (a not in dic.keys()):
        dic[a] = b_ko
    else:
        dic[a] = dic[a] + b_ko

sorted_dic = sorted(dic.items(), key=lambda x: x[0])
number = 0

if (K_ban == 1):
    print(sorted_dic[0][0])
else:
    for i in range(len(sorted_dic)):
        number += sorted_dic[i][1]
        
        if (number >= K_ban):
            print(sorted_dic[i][0])
            break
