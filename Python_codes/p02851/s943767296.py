from itertools import accumulate
n,k = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a
a2 = list(accumulate(a))

sa = dict()
ans = 0
l = 0
for i in range(n+1):
    saadd = (i-a2[i]) % k
    try:
        sa[saadd] += 1
    except:
        sa[saadd] = 1
    l += 1
    if l < k:
        continue
    nowidx = i-k+1
    now = (nowidx-a2[nowidx])% k
    try:
        ans += sa[now]-1
    except:
        pass
    sa[now] -= 1
    l -= 1




for val,cnt in sa.items():
    ans += cnt*(cnt-1)//2


print(ans)