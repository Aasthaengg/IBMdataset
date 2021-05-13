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
a = inl()
c = [a[i]-i-1 for i in range(n)]
c.sort()
mn = s = sum(c[1:])-(n-1)*c[0]
for i in range(n-1):
    s += (2*i+2-n)*(c[i+1]-c[i])
    mn = min(mn,s)
print(mn)
