from sys import exit
from itertools import accumulate,chain
n,*s=open(0).read().split()
t=[2*i.count("(")-len(i) for i in s]
if sum(t)!=0:
    print("No");exit()
#pypyではinitialだめ
st=[[min(accumulate(s_,lambda a,b: a+(1 if b=="(" else -1),initial=0)),t_] for s_,t_ in zip(s,t)]

now=0
v=list(filter(lambda x:x[1]>=0,st))
w=list(filter(lambda x:x[1]<0,st))
v.sort()
w.sort(key=lambda z:z[1]-z[0])

for c in chain(v[::-1],w[::-1]):
    if now+c[0]<0:
        print("No");exit()
    now+=c[1]
print("Yes")