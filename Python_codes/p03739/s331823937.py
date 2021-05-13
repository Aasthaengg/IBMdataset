import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

cum = As.pop(0)
if cum!=0:
    cum2 = cum
    ans = 0
    for a in As:
        if cum*(cum+a)>=0:
            ans += abs(cum+a)+1
            cum = -1 if cum>0 else 1
        else:
            cum += a
        
    ans2 = abs(cum2)+1
    cum2 = 1 if cum2<0 else -1
    for a in As:
        if cum2*(cum2+a)>=0:
            ans2 += abs(cum2+a)+1
            cum2 = -1 if cum2>0 else 1
        else:
            cum2 += a
    print(min(ans, ans2))
else:
    cum = -1
    ans = 1
    for a in As:
        if cum*(cum+a)>=0:
            ans += abs(cum+a)+1
            cum = -1 if cum>0 else 1
        else:
            cum += a
        
    ans2 = 1
    cum2 = 1
    for a in As:
        if cum2*(cum2+a)>=0:
            ans2 += abs(cum2+a)+1
            cum2 = -1 if cum2>0 else 1
        else:
            cum2 += a
    print(min(ans, ans2))