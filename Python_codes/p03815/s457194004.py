x=int(input())
c=2*((x-1)//11)
#print(c)
y=x-11*c//2
#print(y)
if y<=6:
    ans=c+1
else:
    ans=c+2
print(ans)