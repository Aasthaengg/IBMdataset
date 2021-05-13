import bisect


n, k = map(int, input().split())
v = list(map(int, input().split()))

res = 0
for toru in range(0, min(k, n) + 1):
    tumeru = k - toru
    for migi in range(0, toru + 1):
        hidari = toru - migi
        ans = v[0:hidari] + v[n - migi:n]        
        ans = sorted(ans)
        ind = bisect.bisect_left(ans, 0)
        res = max((sum(ans) - sum(ans[0:min(ind, tumeru)])), res)
print(res) 