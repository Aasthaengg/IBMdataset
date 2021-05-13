n=int(input())
k=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(n):
  if a[i]<=k//2:
    sum+=a[i]
  else:
    sum+=k-a[i]
sum*=2
print(sum)