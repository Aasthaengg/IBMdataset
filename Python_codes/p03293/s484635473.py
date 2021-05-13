import sys
import collections
s=input()
t=input()
s2=collections.deque([])
for i in s:
  s2.append(i)
for i in range(len(s)):
  if ''.join(s2)==t:
    print('Yes')
    sys.exit()
  c=s2.popleft()
  s2.append(c)
print('No')