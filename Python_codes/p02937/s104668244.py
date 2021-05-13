import sys
input = sys.stdin.readline
s = input().strip()
t = input().strip()
chk = [[] for i in range(26)]
ma = [0]*26
ex = [False]*26
for i,si in enumerate(s):
  num = ord(si)-97
  chk[num].append(i+1)
  if not ex[num]:
    ex[num] = True
  ma[num] = i+1
  
import math,bisect
now = 0
ans = 0
l = len(s)
for i,ti in enumerate(t):
  ans += 1
  j = i+1
  n = ord(ti)-97
  if not ex[n]:
    ans = -1
    break
  if ans > now*l + ma[n]:
    now = math.ceil((ans-ma[n])/l)
  ind = bisect.bisect_left(chk[n],ans-now*l)
  ans = chk[n][ind] + now*l
print(ans)