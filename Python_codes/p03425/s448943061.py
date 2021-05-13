import sys
input=sys.stdin.readline
m=0
a=0
r=0
c=0
h=0

n=int(input())
for i in range(n):
    p=input()
    if p[0]=="M":
        m+=1
    elif p[0]=="A":
        a+=1
    elif p[0]=="R":
        r+=1
    elif p[0]=="C":
        c+=1
    elif p[0]=="H":
        h+=1

ans=0
ans+=m*a*r
ans+=m*a*c
ans+=m*a*h
ans+=m*r*c
ans+=m*r*h
ans+=m*c*h
ans+=a*r*c
ans+=a*r*h
ans+=a*c*h
ans+=r*c*h
print(ans)