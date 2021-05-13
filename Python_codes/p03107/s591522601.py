s=list(map(int,list(input())))
from collections import Counter
s+=[0,1]
cs=Counter(s)
print(min(cs.values())*2-2)