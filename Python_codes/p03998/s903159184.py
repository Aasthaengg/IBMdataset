import collections
import sys
sa=input()
sb=input()
sc=input()
a=collections.deque([])
b=collections.deque([])
c=collections.deque([])
for i in range(len(sa)):
  a.append(sa[i])
for i in range(len(sb)):
  b.append(sb[i])
for i in range(len(sc)):
  c.append(sc[i])
current='a'
while True:
  if current=='a':
    if a:
      current=a.popleft()
    else:
      print('A')
      sys.exit()
  if current=='b':
    if b:
      current=b.popleft()
    else:
      print('B')
      sys.exit()
  if current=='c':
    if c:
      current=c.popleft()
    else:
      print('C')
      sys.exit()
