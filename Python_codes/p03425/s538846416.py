from collections import Counter 
from itertools import combinations
n=int(input())
s=[]
count=0
for _ in range(n):
    si=list(input())
    if si[0]=="M" or si[0]=="R" or si[0]=="A" or si[0]=="C" or si[0]=="H":

        s.append(si[0])
s_counter=Counter(s)
s_key=s_counter.keys()
if len(s_key)>=3:
    for i,j,k in combinations(s_key,3):
        count+=s_counter[i]*s_counter[j]*s_counter[k]
print(count)