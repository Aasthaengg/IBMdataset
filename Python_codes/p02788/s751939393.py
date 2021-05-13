# F - Silver Fox vs Monster
N,D,A = map(int,input().split())
XH = [0]*N
for i in range(N):
    X,H = map(int,input().split())
    XH[i] = (X,(H-1)//A+1)
XH = sorted(XH, key=lambda x:x[0])
X = [xh[0] for xh in XH]
M = [XH[0][1]]+[XH[i][1]-XH[i-1][1] for i in range(1,N)]
Y = [0]*N
r = 0
for l in range(N):
    r = max(r,l+1)
    while r<N and X[r]<=X[l]+2*D:
        r += 1
    Y[l] = r-1
ans = 0
tmp = 0
for i in range(N):
    tmp += M[i]
    if tmp>0:
        ans += tmp
        r = Y[i]+1
        if r<N:
            M[r] += tmp
        tmp = 0
print(ans)