from collections import Counter
a=list(input())
ans=len(a)*(len(a)-1)//2
c=Counter(a)
for i in c:
    ans-=c[i]*(c[i]-1)//2
print(ans+1)
