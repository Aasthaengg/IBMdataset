from itertools import permutations
from sys import exit
S=input()
for s in permutations('abc'):
  if S == ''.join(s):
    print('Yes')
    exit(0)
print('No')