import sys
input = sys.stdin.readline
h,w = map(int,input().split())
chk = []
for i in range(h):
  a = list(input().strip())
  for j in a:
    chk.append(j)
    
from collections import Counter
c = Counter(chk)
ans = 'Yes'
cnt = 0
q = 0

if h%2 == 0 and w%2 == 0:
  for i in c.values():
    if i%4 != 0:
      ans = 'No'
      break
      
elif h%2 == 0 and w%2 == 1:
  for i in c.values():
    if i%2 != 0:
      ans = 'No'
      break
    if i%4 == 2:
      cnt += 1
    if cnt > h//2:
      ans = 'No'
      break
    
elif w%2 == 0 and h%2 == 1:
  for i in c.values():
    if i%2 != 0:
      ans = 'No'
      break
    if i%4 == 2:
      cnt += 1
    if cnt > w//2:
      ans = 'No'
      break
      
elif h%2 == 1 and w%2 == 1:
  for i in c.values():
    if i%2 != 0:
      q += 1
    if q > 1:
      ans = 'No'
      break
    if i%4 == 2:
      cnt += 1
    if cnt > h//2+w//2:
      ans = 'No'
      break
      
print(ans)