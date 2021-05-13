import sys
input = sys.stdin.readline
INF = 10**11
A,B,Q = map(int,input().split())
s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]
def binary_search(lis,x):
    ok = 0
    ng = len(lis)-1
    while ng-ok > 1:
        mid = (ok+ng)//2
        if lis[mid] < x:
            ok = mid
        else:
            ng = mid
    return ok
#print(s,t)
for _ in range(Q):
    x = int(input())
    ps = binary_search(s,x)
    pt = binary_search(t,x)
    ans = INF
    #print(ps,pt)
    for i in range(ps,ps+2):
        for j in range(pt,pt+2):
            ds = x - s[i]
            dt = x - t[j]
            
            if (ds < 0 and dt < 0) or (ds > 0 and dt > 0):
                ans = min(ans,max(abs(ds),abs(dt)))
            else:
                ans = min(ans,abs(ds)+abs(dt)+min(abs(ds),abs(dt)))
    print(ans)  
            
