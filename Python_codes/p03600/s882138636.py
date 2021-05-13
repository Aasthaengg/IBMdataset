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
    a.append(inl())
c = [[True]*n for i in range(n)]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if a[i][j] > a[i][k]+a[k][j] or \
               a[i][k] > a[i][j]+a[j][k] or \
               a[k][j] > a[k][i]+a[i][j]:
                print(-1)
                exit()
            elif a[i][j] == a[i][k]+a[k][j]:
                c[i][j] = False
            elif a[i][k] == a[i][j]+a[j][k]:
                c[i][k] = False
            elif a[k][j] == a[k][i]+a[i][j]:
                c[j][k] = False
sm = 0
for i in range(n-1):
    for j in range(i+1,n):
        if c[i][j]:
            sm += a[i][j]
print(sm)
