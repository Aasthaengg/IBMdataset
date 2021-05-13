n,m = map(int,input().split())
nn = n-1
mm = m-1
XList = list(map(int,input().split()))
YList = list(map(int,input().split()))

XDiff = [0] * nn
YDiff = [0] * mm
for i in range(nn):
    XDiff[i] = XList[i+1]-XList[i]
for i in range(mm):
    YDiff[i] = YList[i+1]-YList[i]

MOD = 10**9+7 
sumx = 0
sumy = 0
for i in range(1,n):
    sumx += (i*(n-i))*XDiff[i-1] 
    sumx %= MOD
for i in range(1,m):
    sumy += (i*(m-i))*YDiff[i-1]
    sumy %= MOD

ans = sumx*sumy%MOD
print(ans)
