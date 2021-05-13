n=int(input())
sum=100000
for i in range(n):
    sum=sum*1.05
    i+=1
    if sum%1000>0:
        sum=sum-sum%1000
        sum+=1000
print(int(sum))
