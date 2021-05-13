from itertools import *
n,*s=open(0).read().split()
st=[[min(accumulate(s_,lambda a,b: a+(1 if b=="(" else -1),initial=0)),2*s_.count("(")-len(s_)] for s_ in s]
now=0
for c,d in chain(sorted([x for x in st if x[1]>=0])[::-1],sorted([x for x in st if x[1]<0],key=lambda z:z[1]-z[0])[::-1]):
    if now+c<0:
        print("No");break
    now+=d
else:
    print("No" if now else "Yes")