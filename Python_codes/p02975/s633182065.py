from functools import reduce
from operator import xor
from collections import Counter
N=int(input())
A=list(map(int, input().split()))
C=Counter(A)
if len(C)==1:
    k=list(C.keys())[0]
    print("YNeos"[k!=0::2])
elif len(C)==2:
    (k1,v1),(k2,v2)=C.most_common(2)
    print("YNeos"[not(v2*2==v1 and k1^k1^k2==0)::2])
else:
    print("YNeos"[not(len(C)==3 and reduce(xor, C.keys())==0 and len(set(C.values()))==1)::2])