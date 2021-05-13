N,M=list(map(int, input().split()))
ans=1
for i in range(1,int(M**0.5)+1):
  if M%i==0:
    j=M//i
    if i>=N:
      ans=max(ans,j)
    if j>=N:
      ans=max(ans,i)
print(ans)