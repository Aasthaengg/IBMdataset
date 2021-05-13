n,k=list(map(int,input().split()))
h=list(map(int,input().split()))
sum=0
for i in range(n):
  if h[i]>=k:
    sum=sum+1
print(sum)