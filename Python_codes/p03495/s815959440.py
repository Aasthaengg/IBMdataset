import sys
from collections import Counter
read=sys.stdin.read

n,k,*a=map(int,read().split())

coa=Counter(a)
da=sorted(list(iter(coa)), key=coa.get)
print(sum(coa[x] for x in da[:len(da)-k]))
