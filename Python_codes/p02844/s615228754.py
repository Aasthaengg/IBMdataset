n=int(input())
s=input()
ans=0
from collections import Counter
c=Counter(s)
for i in range(1000):
    x=str(i)
    if len(x)==1:
        x="00"+x
    elif len(x)==2:
        x="0"+x
    k=0
    for j in range(n):
        if s[j]==x[k]:
            k+=1
        if k==3:
            ans+=1
            break
        
print(ans)
