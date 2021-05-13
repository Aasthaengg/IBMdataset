t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

L1 = t1*a1+t2*a2
L2 = t1*b1+t2*b2
if L1 == L2:
    print('infinity')
    exit()
if t1*a1 == t1*b1:
    print(1)
    exit()

flg = 1 if L1 < L2 else 0
ok = 0
ng = 10**15+1
mid = (ok + ng)//2
ev = 0
while ng - ok > 1:
    #print(mid * L1 - t2*a2, mid * L2 - t2*b2)
    if mid * L1 - t2*a2 > mid * L2 - t2*b2:
        if flg:
            ok = mid
        else:
            ng = mid
    elif mid * L1 - t2*a2 == mid * L2 - t2*b2:
        ok = mid
        ev = 1
        break
    else:
        if flg:
            ng = mid
        else:
            ok = mid
    mid = (ok + ng)//2
if ok == 0:
    print(0)
    exit()
if ev:
    print((ok-1) * 2)
else:
    print(ok * 2 - 1)
