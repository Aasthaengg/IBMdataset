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

x = ins()
s = []
for c in x:
  s.append(c)
  while len(s)>1 and s[-2]=='S' and s[-1]=='T':
    s.pop()
    s.pop()
print(len(s))
