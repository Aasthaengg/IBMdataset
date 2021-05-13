n=int(input())
d=0
x=[0 for i in range(n)]
y=[0 for i in range(n)]
for i in range(n):
    x[i],y[i]=map(int,input().split())

for i in range(n-2):
    if(x[i]==y[i] and x[i+1]==y[i+1] and x[i+2]==y[i+2]):
        d=d+1
    else:
        d=d
if(d>0):
    print("Yes")
else:
    print("No")