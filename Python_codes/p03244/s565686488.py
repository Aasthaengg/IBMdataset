from collections import Counter

n, *v = map(int, open(0).read().split())
vo = Counter(v[::2])
ve = Counter(v[1::2])
vo_mc = vo.most_common()[0]
ve_mc = ve.most_common()[0]
if vo_mc[0] == ve_mc[0]:
    if vo_mc[1] > ve_mc[1]:
        ans = n//2 - vo_mc[1]
        if ve_mc[1] != n//2:
            ans += n//2 - ve.most_common()[1][1]
        else:
            ans += n//2
    elif vo_mc[1] < ve_mc[1]:
        ans =  n//2 - ve_mc[1]
        if vo_mc[1] != n//2:
            ans += n//2 - vo.most_common()[1][1]
        else:
            ans += n//2
    else:
        ans = n
        if ve_mc[1] != n//2:
            ans = min(n//2 - vo_mc[1] + n//2 - ve.most_common()[1][1], ans)
        if vo_mc[1] != n//2:
            ans = min(n//2 - vo.most_common()[1][1] + n//2 - ve_mc[1], ans)
        ans = min(n//2 - vo_mc[1] + n//2, ans)
else:
    ans = n//2 - vo_mc[1] + n//2 - ve_mc[1]
print(ans)