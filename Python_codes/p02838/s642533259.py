s=[0 for i in range(60)]
def totwo(x):
  return [int(x&(2**i)>0) for i in range(60)]

n=int(input())
a=list(map(lambda x:totwo(int(x)),input().split()))

d=[a[0][i] for i in range(60)]
for i in range(1,n):
  for j in range(60):
    if a[i][j]:
      s[j]+=i-d[j]
    else:
      s[j]+=d[j]
    d[j]+=a[i][j]

ss=0
r=1
mod=10**9+7
for i in range(60):
  ss=(ss+r*s[i])%mod
  r=(r*2)%mod
print(ss)

