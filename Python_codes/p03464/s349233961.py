import sys
import math

k = int(input())
a = list(map(int,input().split()))

if a[-1] != 2:
    print(-1)
    sys.exit()
else:
    mi,ma = 2,2
    for i in range(k-1,-1,-1):
        if mi == ma and mi%a[i] != 0 :
            print(-1)
            sys.exit()
        elif mi != ma and math.floor(ma/a[i]) - math.floor((mi-1)/a[i]) == 0:
            print(-1)
            sys.exit()
        else:
            mi = math.ceil(mi / a[i]) * a[i]
            ma = math.floor(ma / a[i]) * a[i] + a[i] - 1
            
    print(mi,ma)