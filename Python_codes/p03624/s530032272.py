import sys
from string import ascii_lowercase as alphabets
from collections import defaultdict

readline=sys.stdin.readline

s=readline().strip()
d=defaultdict(int)
for x in s:
  d[x]=1
for a in alphabets:
  if d[a]==0:
    print(a)
    sys.exit()
print('None')