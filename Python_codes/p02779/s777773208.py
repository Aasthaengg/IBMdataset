import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

c=len(Counter(a))
if n==c:
  print('YES')
  
else:
  print('NO')