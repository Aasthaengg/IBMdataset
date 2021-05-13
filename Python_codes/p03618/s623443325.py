import collections
a=input()
c=collections.Counter(a)
l=len(a)
s=-1
for i in c.values():s+=i*(i-1)//2
print(l*(l-1)//2-s)