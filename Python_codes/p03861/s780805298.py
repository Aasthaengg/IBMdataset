a,b,c=map(int,input().split())
n=a//c
m=b//c
o=0
if a%c==0:
    o=1
print(m-n+o)
