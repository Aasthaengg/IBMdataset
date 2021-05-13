#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split()) 
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

sx,sy,tx,ty = inm()
p = 'L'
p += 'U'*(ty+1-sy)
p += 'R'*(tx+1-sx)
p += 'D'
p += 'L'*(tx-sx)
p += 'D'*(ty-sy)
p += 'R'*(tx-sx)
p += 'U'*(ty-sy)
p += 'R'
p += 'D'*(ty+1-sy)
p += 'L'*(tx+1-sx)
p += 'U'
print(p)

