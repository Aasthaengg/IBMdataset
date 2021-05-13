from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**19
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,k = inm()
x = []
y = []
for i in range(n):
    xx,yy = inm()
    x.append(xx)
    y.append(yy)
mn = BIG
for i in range(n-1):
    for j in range(i+1,n):
        xn = min(x[i],x[j])
        xx = max(x[i],x[j])
        for ii in range(n-1):
            for jj in range(ii+1,n):
                yn = min(y[ii],y[jj])
                yx = max(y[ii],y[jj])
                cnt = 0
                for m in range(n):
                    if xn<=x[m]<=xx and yn<=y[m]<=yx:
                        cnt += 1
                if cnt>=k:
                    mn = min(mn, (xx-xn)*(yx-yn))
print(mn)
