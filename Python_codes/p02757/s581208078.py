from collections import defaultdict
n,p = [int(x) for x in input().split()]
s = input()
if p!=2 and p!=5:
  r = defaultdict(int)
  a = int(s)
  r[a%p]+=1
  for i in range(n):
    a = (a%p-int(s[i])%p*pow(10,(n-1-i),p))%p
    r[a]+=1
  #print(r)
  ans = 0
  cnt=1
  for i in r.values():
    ans+=i*(i-1)//2
  print(ans)
elif p==2:
  ans = 0
  for i in range(n):
    if int(s[i])%2==0:
      ans +=i+1
  print(ans)
elif p==5:
  ans = 0
  for i in range(n):
    if int(s[i])%5==0:
      ans +=i+1
  print(ans)