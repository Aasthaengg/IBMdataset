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
    if len(a)>=2 and a[-1]>a[-2]+1:
        print(-1)
        exit()
if a[0]!=0:
    print(-1)
    exit()
cnt = 0
for i in range(1,n):
    if i==n-1:
        cnt += a[n-1]
    if a[i]!=a[i-1]+1:
        cnt += a[i-1]
print(cnt)
