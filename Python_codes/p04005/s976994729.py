a,b,c=map(int,input().split())
mina=0
minb=0
minc=0

if a%2==1:
    mina=b*c
else:
    mina=0
if b%2==1:
    minb=c*a
else:
    minb=0
if c%2==1:
    minc=a*b
else:
    minc=0

print(min(mina,minb,minc))