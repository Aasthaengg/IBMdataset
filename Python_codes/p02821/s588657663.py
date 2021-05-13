#幸福度の最小値で二分探索

##右手左手による重複の処理
##同一の値や和がたまたま一致する重複の処理
import bisect
n,m = map(int, input().split())
a = list(map(int, input().split( )))
a.sort()
a2 = [a[i]*2 for i in range(n)]

mn = -1
mx = (a[-1]+1)*2
md = (mx+mn)//2
while mx-mn>1:
    md = (mx+mn)//2
    cnt = 0
    for i in range(n):
        tmp = md-a[i]
        idx = bisect.bisect_left(a, tmp)
        cnt += n-idx

    if cnt >= m:
        mn = md
    else:
        mx = md
ans = 0

acc = []
sm = 0
for i in range(n):
    sm += a[i]
    acc.append(sm)
acc.append(0)##一つも足さない場合
#iは右手とする
for i in range(n-1,-1,-1):
    idx = bisect.bisect_left(a,mx-a[i])
    tmp2 = n-idx
    if m>=tmp2:
        ans += a[i] * tmp2
        ans += (acc[n-1] - acc[idx-1])
        m-=tmp2
    else:
        ans += a[i]*m
        ans += acc[n-1]-acc[n-1-m]
        break
if m:
    ans += mn*m

print(ans)
    

    
