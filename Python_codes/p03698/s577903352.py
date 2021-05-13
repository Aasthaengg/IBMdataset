from collections import Counter
import sys

s=Counter(input())
for x in iter(s):
  if s[x]>1:
    print('no')
    sys.exit()
print('yes')

  

