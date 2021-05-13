S=input()
T=input()
from collections import*
cs=Counter(S)
ct=Counter(T)
csv=sorted(cs.values())
ctv=sorted(ct.values())
print('YNeos'[csv!=ctv::2])