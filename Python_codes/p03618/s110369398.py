from collections import Counter
a=input()
c=Counter(a)
n=len(a)
if n==1:print(1)
else:
    ans=n*(n-1)//2
    for i in c.values():
        if i==1:continue
        else:ans-=i*(i-1)//2
    print(ans+1)
