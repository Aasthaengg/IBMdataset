a,b=map(int, input().split())

dif=b-a
sum=0

for i in range(1,dif):
    sum+=i
    
print(sum-a)    