n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sm=sum(a)

cnt=0
rest=0

for i in range(n):
    a[i]=max(0,a[i]-rest)
    rest=0
    rest=max(0,b[i]-a[i])
    a[i]=max(0,a[i]-b[i])
a[n]=max(0,a[n]-rest)

print(sm-sum(a))
