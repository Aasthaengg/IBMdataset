import re
S=input()
m=re.findall('(R+L+)',S)
A=[]
for s in m:
    r=len(s.split('L')[0])
    A.append((r,len(s)-r))
res=[]
for l,r in A:
    L=(l+1)//2+r//2
    R=l//2+(r+1)//2
    res+=[0]*(l-1)+[L,R]+[0]*(r-1)
print(*res)