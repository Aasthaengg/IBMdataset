n=int(input())
a=list(map(int,input().split()))
ans=0
for (i,j) in zip(range(n),a):
  if i==a[j-1]-1:
    ans+=1
print(ans//2)