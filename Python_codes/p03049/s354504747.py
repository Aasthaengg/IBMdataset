n = int(input())
s = [input() for _ in range(n)]

import re
cnt = 0
for i in range(n):#ABでなくAAだと無理だがこれで
    cnt += len(re.findall("AB",s[i]))
    si = s[i].replace("AB","x")
    s[i] = si
ac= 0
bc = 0
abc = 0
for i in range(n):
    if s[i]:
        if  s[i][-1]=="A" and s[i][0]=="B":
            abc+=1
        elif s[i][-1]=="A":
            ac+=1
        elif s[i][0]=="B":
            bc+=1
        
#############
mn=min(ac,bc)
cnt += mn
if ac or bc:
    cnt += abc
else:
    cnt+=max(abc-1,0)
print(cnt)
