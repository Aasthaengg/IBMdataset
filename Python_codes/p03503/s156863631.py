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

n = inn()
f = []
p = []
for i in range(n):
    f.append(inl())
for i in range(n):
    p.append(inl())
mx = -BIG
for t in range(1,2**10):
    s = [(t>>i)%2 for i in range(10)]
    sm = 0
    for i in range(n):
        x = sum([s[j]*f[i][j] for j in range(10)])
        sm += p[i][x]
    mx = max(mx,sm)
print(mx)
