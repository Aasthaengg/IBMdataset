x=int(input())
c=x//11*2
m=x%11
if m==0:print(c)
elif m<=6:print(c+1)
else:print(c+2)