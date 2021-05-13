s = input()
import re
import math
ans = [0]*len(s)
a = [i.start() for i in re.finditer("RL",s)]

l_side = 0
r_side = 0
for i in range(len(a)-1):
    
    
    if s[a[i]+2:a[i+1]].find("R") != -1:
        r_side = a[i]+1 + s[a[i]+2:a[i+1]].find("R") 
        ans[a[i]+1] =math.ceil((a[i] - l_side)  / 2) + ((r_side - a[i]-1)//2) + 1
        ans[a[i]] = ((a[i] - l_side)  // 2) + math.ceil((r_side - a[i]-1)/2)+1
        
    else:
        r_side = a[i+1]-1
        ans[a[i]+1] = math.ceil((a[i] - l_side)  / 2) + ((r_side - a[i]-1)//2) + 1
        ans[a[i]] = ((a[i] - l_side)  // 2) + math.ceil((r_side - a[i]-1)/2)+1
    l_side = r_side+1
    
#最後に
ans[a[-1]+1] = math.ceil((a[-1] - l_side)  / 2) + ((len(s) - a[-1]-2)//2) + 1
ans[a[-1]] =   ((a[-1] - l_side)  // 2) + math.ceil((len(s) - a[-1]-2)/2)+1
L=[str(a) for a in ans]
L=" ".join(L)
print(L)