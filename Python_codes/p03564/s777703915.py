n=int(input())
k=int(input())
ans=float('inf')
for i in range(2**n):
  c=1
  tmp=format(i, '0'+str(n)+'b')
  for j in tmp:
    if j=='0':
      c*=2
    else:
      c+=k
      
  ans=min(c, ans)
  
print(ans)