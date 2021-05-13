import collections
from collections import Counter
N=int(input())
a=input().split()
A=[int(number) for number in a]
pluss=[]
minuss=[]
number=1
for a in A:
    plus=a+number
    minus=number-a
    pluss.append(plus)
    minuss.append(minus)
    number+=1

m=Counter(minuss)

answer=0
for p in pluss:
    if p in m.keys():
        answer+=m[p]
print(answer)
