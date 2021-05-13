n=int(input())
sum=0
a=[0]*n

b=list(map(int,input().split()))
a[0]=b[0]
a[n-1]=b[n-2]
sum=a[0]+a[n-1]
for i in range(n-2):
    sum=sum+min(b[i],b[i+1])
print(sum)