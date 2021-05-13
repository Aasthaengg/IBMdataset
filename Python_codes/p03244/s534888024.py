from collections import Counter

n=int(input())
v=list(map(int,input().split()))

e=Counter(v[0::2])
o=Counter(v[1::2])
e_key=sorted(e.items(),reverse=True,key=lambda x:x[1])
o_key=sorted(o.items(),reverse=True,key=lambda x:x[1])

if e_key[0][0]!=o_key[0][0]: print(n-e_key[0][1]-o_key[0][1])
else:
    if len(e_key)==1 and len(o_key)==1: print(n//2)
    elif len(e_key)==1: print(n//2-o_key[1][1])
    elif len(o_key)==1: print(n//2-e_key[1][1])
    else:
        if e_key[0][1]>o_key[0][1]: print(n-e_key[0][1]-o_key[1][1])
        elif e_key[0][1]<o_key[0][1]: print(n-o_key[0][1]-e_key[1][1])
        else:
            if e_key[1][1]>o_key[1][1]: print(n-e_key[1][1]-o_key[0][1])
            else: print(n-o_key[1][1]-e_key[0][1])