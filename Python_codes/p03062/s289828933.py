n = int(input())
a = list(map(int,input().split()))
import bisect
a.sort()

idx = bisect.bisect_left(a, 0)
sm = [abs(x) for x in a]
if idx % 2 == 0:
    print(sum(sm))
else:
    print(sum(sm) - 2*min(sm))