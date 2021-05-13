MOD=10**9+7
n,m=map(int,input().split())
a=set([int(input()) for _ in range(m)])
if 1 in a:
  ans=[1,0]
else:
  ans=[1,1]

for i in range(1,n):
  if i+1 in a:
    ans.append(0)
  else:
    s=(ans[-1]+ans[-2])%MOD
    ans.append(s)
print(ans[-1]%MOD)