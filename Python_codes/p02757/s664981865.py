from collections import defaultdict,deque
import itertools
n,p = [int(x) for x in input().split()]
s = list(input())
if p!=2 and p!=5:
  r = defaultdict(int)
  a =[]
  s1 = s[::-1]
  for i in range(n):
    a.append((int(s1[i])%p*pow(10,i,p))%p)
  a = [0]+a[::-1]
  b = list(itertools.accumulate(a))
  for i in b:
    r[i%p]+=1
  ans = 0
  for i in r.values():
    ans+=(i*(i-1))//2
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
