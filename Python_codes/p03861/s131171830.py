a,b,x=map(int,input().split())

if a%x==0:
    p=1
else:
    p=0

print(p+b//x-a//x)