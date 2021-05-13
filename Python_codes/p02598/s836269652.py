N, K = map(int, input().split())
A = list(map(int, input().split()))
ok = 10**9
ng = 0
while ng+1 < ok:
    tmp = (ok+ng)//2
    k = 0
    for a in A:
        if a%tmp == 0:
            k += a//tmp -1
        else:
            k += a//tmp
    if k <= K:
        ok = tmp
    else:
        ng = tmp
print(ok)