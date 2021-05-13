n=int(input())
ans=0
for i in range(1,int(n**.5+(n**.5%1!=0))):
  j=(n-i)//i
  if n%j==n//j:
    ans+=j
print(ans)