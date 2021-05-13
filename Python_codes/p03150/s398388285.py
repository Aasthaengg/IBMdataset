import re

s = input()
key = 'keyence'
ans = 'NO'
for i in range(len(key)):
    k1 = key[:i + 1]
    k2 = key[i + 1:]
    
    k1_temp = [m.span() for m in re.finditer(k1, s)]
    for j in range(len(k1_temp)):
        k2_temp= [m.span() for m in re.finditer(k2, s)]
        for k in range(len(k2_temp)):
            if k1_temp[j][1] == k2_temp[k][0]:
                ans = 'YES'
                break
            if  k1_temp[j][0] == 0 and k2_temp[k][1] == len(s):
                ans = 'YES'
                break
print(ans)
