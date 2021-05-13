N,K = map(int,input().split())
x = list(map(int,input().split()))

start = N
for i in range(N):#０より大きい最初のところをstartとする
    if x[i]>0:
        start = i
        break
x.insert(start,0)

ans = float("inf")
for i in range(0,K+1,1):#左側をいくつとるか
    j = K-i#右側はj個とることになる

    if 0 <= start-i and start+j<=N:
        tmpans = x[start+j]-x[start-i]+min(x[start+j],-x[start-i])
        ans = min(ans,tmpans)
print(ans)
