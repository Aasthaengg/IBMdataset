num = int(input())
lis = list(map(int,input().split()))
sum = 0
min = lis[0]
max = lis[0]
for i in range(num):
    if(min > lis[i]):min = lis[i]
    if(max < lis[i]):max = lis[i]
    sum = sum+lis[i]
    
print("%d %d %d" %(min,max,sum))
