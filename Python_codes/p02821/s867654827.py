def isok(arg):
    x = 0
    for i in a:
        if arg - i >= 0:
            if arg-i <= 10**5:
                x += cs[arg-i]
        else:
            x += n
    if x >= m:
        return True
    else:
        return False

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if isok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n,m = map(int,input().split())
a = list(map(int,input().split()))
cs = [0]*(10**5+1)
for i in a:
    cs[i] += 1
for i in range(10**5):
    cs[10**5-i-1] += cs[10**5-i]
h = bisect(10**5*2+1,0)
count = 0
ans = 0
for i in a:
    num = max(0,h-i)
    if num <= 10**5:
        ans += 2*i*cs[num]
        count += cs[num]
ans -= (count-m)*h
print(ans)
