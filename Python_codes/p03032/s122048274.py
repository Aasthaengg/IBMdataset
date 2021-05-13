import copy

n, k = map(int,input().split())
v = list(map(int,input().split()))

ans = 0

for l in range(0,n+1):
    for r in range(0,n+1):
        if l+r > n or l+r > k or l+r==0:
            continue
        vc = copy.deepcopy(v)
        have = []
        ll = copy.deepcopy(l)
        rr = copy.deepcopy(r)
        while ll:
            tmp = vc.pop(0)
            have.append(tmp)
            ll -= 1
        while rr:
            tmp = vc.pop(-1)
            have.append(tmp)
            rr -= 1
        have.sort()
        kk = copy.deepcopy(k)
        while have[0] < 0 and kk-(l+r) > 0:
            tmp = have.pop(0)
            kk -= 1
            if not have:
                break
        ans = max(ans, sum(have))
print(ans)