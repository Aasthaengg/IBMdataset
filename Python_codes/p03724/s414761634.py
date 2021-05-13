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

n,m = inm()
d = [0]*(n+1)
for i in range(m):
    a,b = inm()
    d[a] += 1
    d[b] += 1
for i in range(n+1):
    if d[i]%2==1:
        print('NO')
        exit()
print('YES')
