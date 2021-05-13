n = int(input())

al = list(map(int, input().split())) 

import itertools
alsum = list(itertools.accumulate(al))

temp1 = 0
temp2 = 0
res = 0
for i in range(n):
    res += al[i]
    if i % 2 ==0:
        if res >0:
            pass
        else:
            y = res*(-1)+1
            temp1 += y
            res =1
    else:
        if res <0:
            pass
        else:
            y = res+1
            temp1 += y
            res = -1
    
res= 0

for j in range(n):
    res += al[j]
    if j % 2 ==0:
        if res <0:
            pass
        else:
            y = res+1
            temp2 += y
            res = -1
    else:
        if res >0:
            pass
        else:
            y = res*(-1)+1
            temp2 += y
            res = 1

print(min(temp1,temp2))