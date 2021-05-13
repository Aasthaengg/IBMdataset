N=int(input())
a=list(map(int,input().split()))
i=1
sum=0
while i<=N:
    if a[i-1]%2!=0:
        sum=sum+1
    i=i+2
print(sum)