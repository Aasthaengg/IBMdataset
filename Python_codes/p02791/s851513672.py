N=int(input())
P=list(map(int, input().split()))
m=9999999
count=0
for i in range(1,N+1):
  if m>=P[i-1]:
    count+=1
    m=P[i-1]
  
print(count)