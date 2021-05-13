from itertools import*
_,*s=open(0)
s=[a[0]!=b[0]for a,b in zip(*map(groupby,s))]
c=3*2**s[0]
for a,b in zip(s,s[1:-1]):c=c*(a+2if b else(1^a)+1)%(10**9+7)
print(c)