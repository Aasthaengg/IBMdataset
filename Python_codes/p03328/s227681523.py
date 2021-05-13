a=list(map(int,input().split()))
sum=0
for i in range(1,a[1]-a[0]):
    sum+=i
print(sum-a[0])