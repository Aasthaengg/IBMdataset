n=int(input())
a=list(map(int,input().split()))

def solve(parity):
  wa=0
  ans=0
  for i in range(n):
    wa+=a[i]
    if i%2==parity:
      if wa>=0:
        ans+=wa+1
        wa-=wa+1
    else:
      if wa<=0:
        ans+=-wa+1
        wa+=-wa+1
  return ans

print(min(solve(0),solve(1)))