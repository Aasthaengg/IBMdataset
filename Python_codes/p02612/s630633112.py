n=int(input())
mod=n%1000
if(mod==0):
  ans=0
else:
  ans=1000-mod
print(ans)