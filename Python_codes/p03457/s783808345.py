N = int(input())
t=[[0,0,0]]
for i in range(N):
    A=list(map(int, input().strip().split()))
    t.append(A)

flag=0
flag2=0
for i in range(N):
    flag=0
    time=t[i+1][0]-t[i][0]
    x=t[i+1][1]-t[i][1]
    y=t[i+1][2]-t[i][2]
    time=abs(time)
    x=abs(x)
    y=abs(y)
    
    if (time-(x+y))%2==0 and time>=(x+y):
        flag=1
    if flag!=1:
        flag2=1    

if flag2==1:
    print("No")
else:
    print("Yes")


