n=int(input())
a=list(map(int,input().split()))
ans=0

for x in range(n):
  b=a[x]
  while b%2==0:
    if b%2==0:
      b=b//2
      ans+=1
      
print(ans)