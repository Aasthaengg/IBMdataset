N,X=map(int,input().split())
a=list(map(int,input().split()))
total=sum(a)
if a[0]>X:
    a[0]=X
for i in range(N-1):
    if a[i]+a[i+1]>X:
        a[i+1]=X-a[i]
print(total-sum(a))