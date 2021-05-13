a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
abc=sorted([a,b,c])
if abc[2]%2==0:
    print(0)
else:
    print(abc[0]*abc[1])