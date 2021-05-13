n, k = map(int, raw_input().split())
logs = map(int, raw_input().split())

l = 0
r = 10**9


def check(v):
    c = k
    for i in logs:
        if i%v==0:
            p=i/v
        else:
            p=i/v+1
        if(p-1 <= c):
            c -= p-1
        else:
            return 0
    return 1


ans = 10**9
while l+1<r:
    mid = (l+r)/2
    if(check(mid)):
        ans = min(ans, mid)
        r = mid
    else:
        l = mid
print ans
