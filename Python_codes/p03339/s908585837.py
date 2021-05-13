import numpy as np
N = int(input())
S = input()
pre_s = S[0]
sum1 = sum(s == 'E' for s in S)
res = sum1
if S[0] =='E':
    sum1-=1
    
for i in range(1,len(S)):
    if pre_s =='W':
        sum1 +=1
    if S[i]=='E':
        sum1 -=1
    if sum1 < res:
        res =sum1
    pre_s = S[i]
print(res)