n=int(input())
x=0
y=0
t=0
f=0
for i in range(n):
    T,a,b=map(int,input().split())
    if not(abs(a-x)+abs(b-y)<=T-t and (abs(a-x)+abs(b-y)-(T-t))%2==0):
        f=1
    x=a
    y=b
    t=T
print("Yes" if f==0 else "No")
