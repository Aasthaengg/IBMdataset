N=int(input())
A_1 = list(map(int, input().split()))
A_2 = list(map(int, input().split()))
sum=0
for k in range(1,N+1):
    sum_2=0
    for i in range(0,k): 
        sum_2=sum_2+A_1[i]
    for j in range(k-1,N):
        sum_2=sum_2+A_2[j]
    if sum<sum_2:    
        sum=sum_2    
print(sum)