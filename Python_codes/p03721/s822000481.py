from collections import defaultdict

n,k = map(int,input().split())
dct = defaultdict(int)
for _ in range(n):
    a,b=map(int,input().split())
    dct[a]+=b
dct = sorted(dct.items())
now=0
for tpl in dct:
    now+=tpl[1]
    if now>=k:
        print(tpl[0])
        break