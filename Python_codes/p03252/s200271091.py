from collections import *
s=input()
r=input()
c=Counter(sorted(s))
C=Counter(sorted(r))
if(sorted(c.values())==sorted(C.values())):
    print("Yes")
else:
    print("No")
