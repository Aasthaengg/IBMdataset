n=int(input())
ls=list(map(int,input().split()))
prev=1
ans=0
for i in range(n):
  k=ls[i]
  if k%2==1:
    ans+=prev*2*(3**(n-i-1))
  else:
    ans+=prev*3**(n-i-1)
    prev*=2
print(ans)