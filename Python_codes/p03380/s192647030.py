n = int(input())
a = list(map(int , input().split()))

a.sort()
import bisect
bl = bisect.bisect_left(a, a[-1]//2)
#print(a[-1], a[bl], a[bl-1])

if abs(a[-1]/2 - a[bl]) < abs(a[-1]/2 - a[bl-1]):
    print(a[-1] , a[bl])
else:
    print(a[-1] , a[bl-1])

