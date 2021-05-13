K = int(input())
As = list(map(int, input().split()))

def f(n):
    for a in As:
        n = a * (n//a)
    return n

ng,ok = 1, 10**20
while ok-ng > 1:
    m = (ok+ng)//2
    if f(m) >= 2: #2以上ならTrue
        ok = m
    else:
        ng = m
mn = ok
# print(ng,ok)

ok,ng = 1, 10**20
while ng-ok > 1:
    m = (ok+ng)//2
    if f(m) <= 2: #2以下の範囲
        ok = m
    else:
        ng = m
mx = ok

# print(ok,ng)
if mn > mx:
    print(-1)
else:
    print(mn,mx)
