n=int(input())
ans=0
for i in range(n):
  x,u=input().split()
  x=float(x)
  if u=="BTC":
    x=x*380000
  ans=ans+x
print(ans)
