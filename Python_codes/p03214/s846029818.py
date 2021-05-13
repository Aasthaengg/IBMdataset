N=int(input())
a=list(map(int,input().split()))
s=sum(a)
t=200
A=0
for i in range(N-1,-1,-1):
    d=abs(a[i]*N-s)
    if d<=t:
        t=d
        A=i
print(A)