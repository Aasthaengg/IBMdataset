import math
ceil = math.ceil
def isok(x):
    syugyo = 0##全員の時間がx以下を達成するための修行回数
    for i in range(n):
        syugyo += max(0,  ceil(( A[i]*F[i]-x )/F[i])  )
    return syugyo>kai
def bisect():
    ok = -1
    ng = 10**12+1 ##最小コストの最大値
    x = (ok+ng)//2
    while ng-ok>1:
        if isok(x):
            ok = x
        else:
            ng = x
        x = (ok+ng)//2
    return ok+1 ##一番右のTrueのindex  Trueの個数はok+1こ


n,kai = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))
F.sort()
A.sort(reverse=True)
print(bisect())
