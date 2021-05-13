a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
ls=[a,b,c]
ls.sort()
print(int(ls[0]*ls[1]/2))