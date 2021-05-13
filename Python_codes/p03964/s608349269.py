n=int(input())

x,y=map(int,input().split())
for i in range(n-1):
    t,a=map(int,input().split())
    k=(x+t-1)//t
    m=(y+a-1)//a
    p=max(k,m)
    x=t*p
    y=a*p
print(x+y)
