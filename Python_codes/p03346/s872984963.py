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

n = inn()
a = []
for i in range(n):
    a.append(inn())
b = [0]*(n+1)
for i in range(n):
    b[a[i]] = b[a[i]-1]+1
print(n-max(b))
