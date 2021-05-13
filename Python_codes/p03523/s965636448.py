from itertools import combinations as c
from itertools import chain

S=list("AKIHABARA") #0,4,6,8
l=[0,4,6,8]
o=set()

for k in chain(c(l,2),c(l,3),c(l,4)):
  b=[j if not i in k else "" for i,j in enumerate(S)]
  o.add("".join(b))
o.add("AKIHABARA")

s=input()
if s in o:
  print("YES")
else:
  print("NO")