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
ab = []
for i in range(n):
    a,b = inm()
    ab.append((a+b,a,b))
ab.sort(reverse=True)
sm = 0
for i in range(n):
    if i%2==0:
        sm += ab[i][1]
    else:
        sm -= ab[i][2]
print(sm)
