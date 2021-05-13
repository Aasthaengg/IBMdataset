n,t=map(int,input().split())
a=list(map(int,input().split()))
sum=0
for i in range(n-1):
    if a[i+1]-a[i]>t:
        sum+=t
    else:
        sum+=a[i+1]-a[i]
sum+=t
print(sum)