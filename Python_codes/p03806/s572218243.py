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

n,ma,mb = inm()
a = []
b = []
c = []
for i in range(n):
    aa,bb,cc = inm()
    a.append(aa)
    b.append(bb)
    c.append(cc)
dp = [[BIG]*(10+1) for i in range(10+1)]
dp[0][0] = 0
for t in range(n):
    dp2 = [[BIG]*(10*(t+1)+1) for i in range(10*(t+1)+1)]
    for i in range(10*t+1):
        for j in range(10*t+1):
            if dp[i][j]<BIG:
                dp2[i][j] = min(dp2[i][j],dp[i][j])
                dp2[i+a[t]][j+b[t]] = min( \
                     dp2[i+a[t]][j+b[t]], dp[i][j]+c[t])
    dp = dp2
mn = BIG
for i in range(1,5000):
    if i*max(ma,mb)>n*10:
        break
    #ddprint(f"i {i} n {n} ma {ma} mb {mb} ima {i*ma}")
    mn = min(mn, dp[i*ma][i*mb])
print(-1 if mn==BIG else mn)
