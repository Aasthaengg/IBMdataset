import sys
N=int(input())
 
t0=0
x0=0
y0=0
 
for i in range(N):
    t,x,y=map(int,input().split())
    l=(t-t0)-abs(x+y-x0-y0)
    t0=t
    x0=x
    y0=y
    if l%2==0 and l>=0:
        continue
    else:
        print("No")
        sys.exit()
print("Yes")