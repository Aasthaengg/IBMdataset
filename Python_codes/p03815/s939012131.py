x=int(input())
count=0
a=x//11
b=x-a*11
if b==0:
    print(a*2)
elif b>=1 and b<=6:
    print(a*2+1)
else:
    print(a*2+2)
