N=int(input())
T=1
A=1
for i in range(N):
    x,y=map(int,input().split())
    d1=1
    d2=1
    if T>x:
        d1=(T-1)//x+1
    if A>y:
        d2=(A-1)//y+1
    T=max(d1,d2)*x
    A=max(d1,d2)*y

print(T+A)