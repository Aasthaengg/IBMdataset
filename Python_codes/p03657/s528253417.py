import sys
a,b=map(int, input().split())
s=[a,b,a+b]
for si in s:
  if si%3==0:
    print('Possible')
    sys.exit()

print('Impossible')
