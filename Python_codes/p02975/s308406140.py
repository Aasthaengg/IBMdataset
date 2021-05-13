# A - XOR Circle
from collections import Counter as ct
n=int(input())
a=list(map(int,input().split()))

c=ct(a)
 
if c[0]==n:
    print("Yes")
elif len(c)==2 and c[0]*3==n:
    print("Yes")
elif len(c)==3 and len(set(c.values()))==1:
    a,b,c = c.keys()
    if (a^b^c)==0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
