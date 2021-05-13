import math
T1,T2=map(int,input().split())
A1,A2=map(int,input().split())
B1,B2=map(int,input().split())
C1,C2=A1-B1,A2-B2
D1,D2=T1*C1,T2*C2

if D1==-D2:
    print("infinity")
    exit(0)

diff=0
x=-1
ans=0

if  D1*(D1+D2)<0:
    ans+=1
    diff+=D1+D2
else:
    print(ans)
    exit(0)

if diff*(diff+D1)<=0:
    ans+=2*abs((diff+D1)//(D1+D2))

if diff+(D1+D2)*abs((diff+D1)//(D1+D2))+D1==0:
    ans+=1
if diff+(D1+D2)*abs((diff+D1)//(D1+D2))+D1+D2==0:
    ans+=1

print(ans)