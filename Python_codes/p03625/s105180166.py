n=int(input())
l=[0,0]
from collections import Counter as co
for k,a in co(list(map(int,input().split()))).items():
    if a>=4:l+=[k,k]
    elif a>=2:l.append(k)
    l.sort()
    l=l[-2:]

print(l[0]*l[1])