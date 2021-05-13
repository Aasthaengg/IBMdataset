r,g,b=map(int,input().split())
k=int(input())
x=0
while g<=r:
    g*=2
    x+=1
while b<=g:
    b*=2
    x+=1
if x<=k:
    print("Yes")
else:
    print("No")