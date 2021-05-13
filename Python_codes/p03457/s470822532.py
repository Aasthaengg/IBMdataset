N=int(input())

t,x,y=0,0,0
F=True
for _ in range(N):
    s,a,b=t,x,y
    t,x,y=map(int,input().split())

    m=abs(x-a)+abs(y-b)
    if not(m<=t-s and (t-s-m)%2==0):
        F=False

if F:
    print("Yes")
else:
    print("No")
        
