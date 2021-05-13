MOD=10**9+7
n,m=map(int,input().split())
a=set([int(input()) for _ in range(m)])
if n==1:
  print(1)
  exit()
if 1 in a and 2 in a:
  print(0)
  exit()
elif 1 in a:
  ans=[0,1]
elif 2 in a:
  ans=[1,0]
else:
  ans=[1,2]

for i in range(2,n):
  if i+1 in a:
    ans.append(0)
  else:
    s=(ans[-1]+ans[-2])%MOD
    ans.append(s)
print(ans[-1]%MOD)