from bisect import *
s = input()
t = input()
pos = {}
for j,i in enumerate(s):
  if i in pos.keys():
  	pos[i].append(j+1)
  else:
    pos[i] = [j+1]
n = len(s)
for i in pos.keys():
  pos[i].append(pos[i][0] + n)
ans = 0
last = 0
for i in t:
  if not i in s:
    print(-1)
    exit()
  last = pos[i][bisect(pos[i],last)]
  if last > n:
    last -= n
    ans += n
print(ans + last)
