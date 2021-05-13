import collections
n=int(input())
c=collections.Counter(list(map(int,input().split())))
p=-1
for x in sorted(c.keys())[::-1]:
    if p==-1 and c[x]>=4:print(x*x);break
    elif p==-1 and c[x]>=2:p=x
    elif p!=-1 and c[x]>=2:print(p*x);break
else:print(0)