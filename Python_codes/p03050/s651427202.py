n=int(input())
ans=0
for i in range(1,int(n**(1/2))+10):
  if (n-i)%i==0 and (n-i)//i>i:
    ans=ans+(n-i)//i
print(ans)