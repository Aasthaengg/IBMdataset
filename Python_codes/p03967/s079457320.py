s=list(input())
n=len(s)
from collections import defaultdict
d=defaultdict(int)
t=['g' if i%2==0 else 'p' for i in range(n)]
pnt=0
for i in range(n):
    if s[i]==t[i]:
        continue
    elif s[i]=='g':
        pnt+=1
    else:
        pnt-=1
print(pnt)