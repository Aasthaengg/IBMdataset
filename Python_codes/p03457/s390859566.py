n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
t_bef=0
x_bef=0
y_bef=0
flag='Yes'

for i in range(1,n+1):
    t,x,y=map(int,input().split())
    dt=t-t_bef
    dist=abs(x-x_bef)+abs(y-y_bef)
    if (dt%2 != dist%2) or dist>dt:
        flag='No'
        break
    t_bef,x_bef,y_bef=t,x,y

print(flag)