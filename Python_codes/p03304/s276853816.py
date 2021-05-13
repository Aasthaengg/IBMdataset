from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,m,d = inm()
if d==0:
    ret = (m-1)/n
else:
    ret = (m-1)*max(0,2.0*(n-d)/(n**2))
print(ret)
