from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7
from collections import defaultdict
def ddprint(x):
  if DBG:
    print(x)

a = ins()
h = defaultdict(int)
for i in range(len(a)):
    h[a[i]] += 1
sm = 1
keys = list(h.keys())
for i,x in enumerate(keys):
    for j in range(i+1,len(keys)):
        sm += h[keys[i]]*h[keys[j]]
print(sm)
