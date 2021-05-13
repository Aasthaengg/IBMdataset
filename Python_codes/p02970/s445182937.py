a,b=[int(x) for x in input().split()]
z=b*2+1
c=a/z
if c%1==0:
    print(a//z)
else:
    print(a//z+1)
