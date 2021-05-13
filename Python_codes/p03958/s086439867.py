k,t=map(int,input().split())
a=list(map(int,input().split()))
sm=sum(a)
n=1
for i in a:
    if i>sm//2:
        n=i-(sm-i)
        break
print(n-1)
