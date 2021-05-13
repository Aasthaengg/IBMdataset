x=int(input())
ans=2*(x//11)
x-=(ans//2)*11
if 0<x<=6:
    ans+=1
elif x==0:
    pass
else:
    ans+=2
print(ans)