N=int(input())
A=list(map(int, input().split()))

zero_A=[0]+A+[0]
dist=[]
for i in range(0, N+1):
   dist.append(abs(zero_A[i]-zero_A[i+1]))
#print(dist)

total=sum(dist)

for i in range(1,N+1):
    if zero_A[i-1]<=zero_A[i]<=zero_A[i+1] or zero_A[i-1]>=zero_A[i]>=zero_A[i+1]:
        print(total)
    else:
        print(total-2*min(dist[i-1], dist[i]))
