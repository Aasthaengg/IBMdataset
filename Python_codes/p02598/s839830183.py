n,k = map(int, input().split())
l = list(map(int,input().split()))
ok = max(l)
ng = 0

def solver(x):
    cnt = 0
    for logs in l:
        if logs % x == 0:
            cnt += (logs // x) -1
        else:
            cnt += logs// x
    if cnt <= k:
        return True
    else:
        return False

while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if solver(mid) == True:
        ok = mid
    else:
        ng = mid

print(ok)
