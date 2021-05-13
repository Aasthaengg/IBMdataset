import collections
a=input()
n=len(a)
A=collections.Counter(a)
v,c = zip(*A.most_common())
ans=n*(n-1)//2
for i in range(len(c)):
    ans-=c[i]*(c[i]-1)//2
print(ans+1)