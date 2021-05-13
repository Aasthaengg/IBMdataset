n=int(input())
x,k=map(int,input().split())
l=list(map(int,input().split()))
m=100000000000000
u=-1
for i in range(n):
    d=x-l[i]*0.006
    if(abs(d-k)<m):
        m=abs(d-k)
        u=i+1
print(u)
