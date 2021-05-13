#from collections import deque,defaultdict
from sys import stdin
input = stdin.readline
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

d = inn()
c = inl()
s = []
for i in range(d):
    s.append(inl())
t = []
for i in range(d):
    t.append(inn()-1)
last = [-1]*26
sm = 0
for i in range(d):
    tt = t[i]
    sm += s[i][tt]
    last[tt] = i
    for j in range(26):
        sm -= c[j]*(i-last[j])
    print(sm)
