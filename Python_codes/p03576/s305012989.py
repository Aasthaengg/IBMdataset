import sys
def LI(): return([int(x) for x in sys.stdin.readline().split()])

N,K = LI()
XY = [LI() for _ in range(N)]

X = []
Y = []
for x,y in XY:
    if not(x in X):
        X.append(x)
    if not(y in Y):
        Y.append(y)
        
X.sort()
Y.sort()
dic_XoYo = {}
dic_XcYo = {}
dic_XoYc = {}
dic_XcYc = {}
for x1 in X:
  for y1 in Y:
    key = x1*(10**10)+y1
    cnt_XoYo = 0
    cnt_XcYo = 0
    cnt_XoYc = 0
    cnt_XcYc = 0
    for x2,y2 in XY:
      if x2<=x1 and y2<=y1:
        cnt_XcYc += 1
      if x2<x1 and y2<=y1:
        cnt_XoYc += 1
      if x2<=x1 and y2<y1:
        cnt_XcYo += 1
      if x2<x1 and y2<y1:
        cnt_XoYo += 1
    dic_XcYc[key] = cnt_XcYc
    dic_XoYc[key] = cnt_XoYc
    dic_XcYo[key] = cnt_XcYo
    dic_XoYo[key] = cnt_XoYo

ans = []
for xl in range(len(X)-1):
  for xr in range(xl,len(X)):
    for yd in range(len(Y)-1):
      for yu in range(yd,len(Y)):
        cnt = dic_XcYc[X[xr]*(10**10)+Y[yu]]
        cnt -= dic_XcYo[X[xr]*(10**10)+Y[yd]]
        cnt -= dic_XoYc[X[xl]*(10**10)+Y[yu]]
        cnt += dic_XoYo[X[xl]*(10**10)+Y[yd]]
        if cnt>=K:
          ans.append((X[xr]-X[xl])*(Y[yu]-Y[yd]))
print(min(ans))

