#AGC016-A
from collections import Counter 
s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

result = []
if len(set(s)) == 1:
    result.append(0)
for i in alphabet:
    s_tmp = s 
    cnt = 0
    for k in range(len(s_tmp)):
        s_new= ""
        for j in range(len(s_tmp)-1):
            if s_tmp[j] == i or s_tmp[j+1] == i:
                s_new += i
            else:
                s_new += s_tmp[j]
        cnt += 1
        if len(set(s_new)) == 1:
            result.append(cnt)
            break        

        s_tmp = s_new
        
            
 

#print(result)
print(min(result))

