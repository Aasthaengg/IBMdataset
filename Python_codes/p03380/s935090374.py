import sys
import bisect
input = sys.stdin.readline

n=int(input())
a=sorted(list(map(int,input().split())))

if n == 2:
    am = a[-1]
    amm = a[0]
else:
    am = max(a)
    ind = bisect.bisect_left(a,am//2)
    am1 = a[ind]
    am2 = a[ind-1]

    am1abs = abs(am/2-am1)
    am2abs = abs(am/2-am2)

    if am1abs <= am2abs:
        amm = am1
    else:
        amm = am2
    
print(am,amm)
