N=int(input())
pret=0
prex=0
prey=0
for i in range(N):
    t,x,y=map(int, input().split())
    d=abs(x-prex)+abs(y-prey)
    dt=t-pret
    if dt >= d and (dt-d)%2==0:
        prex=x
        prey=y
        pret=t
    else:
        
        print("No")
        exit()
print("Yes")
