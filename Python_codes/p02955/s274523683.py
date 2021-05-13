n,k = map(int,input().split())
a = list(map(int,input().split()))
s = sum(a)
div = []
rdiv = []
for i in range(1,int(s**.5+1)):
  if s % i == 0:
    div.append(i)
    rdiv.append(s//i)
if s == int(s**.5)**2:
  div = di[:-1]
rdiv.reverse()
div += rdiv
div.reverse()
#print(div)
for i in range(len(div)):
  now = div[i]
  tmp = []
  for x in a:
    tmp.append(x%now)
  tmp.sort()
  b = n - sum(tmp) // now
  #print(now,tmp,b)
  ans = 0
  for j in range(b):
    ans += tmp[j]
  if ans <= k:
    print(now)
    break