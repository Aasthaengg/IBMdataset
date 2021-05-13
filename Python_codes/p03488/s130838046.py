from collections import deque
import sys
sys.setrecursionlimit(10**8)

def dp(dp_l,i,N,xs,cum,now):
    if i == N:
        if now == 0:
            return True
        return False
    if abs(now) > cum[i]:
        return False
    if dp_l[i][abs(now)] != -1:
        return dp_l[i][abs(now)]
    dp_l[i][abs(now)] = dp(dp_l,i+1,N,xs,cum,now+xs[i]) or dp(dp_l,i+1,N,xs,cum,now-xs[i])
    return dp_l[i][abs(now)]

def check():
    S = input()
    x, y = map(int, input().split())
    fs = list(map(len,S.split('T')))
    if len(fs)<3:
        if x != fs[0]:
            return False
        if len(fs)==1:
            if y == 0:
                return True
            else:
                return False
        if y != fs[1] and y != -fs[1]:
            return False
        return True
    xs = fs[2::2]
    ys = fs[1::2]
    xs.sort(reverse = True)
    N = len(xs)
    M = len(ys)
    cum = [0]*(N+1)
    for i in range(N-1,-1,-1):
        cum[i] = cum[i+1]+xs[i]
    dp_l = [[-1]*(cum[0]+1) for _ in range(N)]
    if not dp(dp_l,0,N,xs,cum,fs[0]-x):
        return False
    ys.sort(reverse = True)
    cum = [ys[-1]]*(M+1)
    for i in range(M-1,-1,-1):
        cum[i] = cum[i+1]+ys[i]
    dp_l = [[-1]*(cum[0]+1) for _ in range(M)]
    if not dp(dp_l,0,M,ys,cum,-y):
        return False
    return True
if check():
    print('Yes')
else:
    print('No')