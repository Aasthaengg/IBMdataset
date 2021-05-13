import bisect
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
mx = a[-1]

idx = bisect.bisect_left(a, mx//2)
if a[idx] == mx//2:
    print(mx, a[idx], sep=" ")
else:
    if a[idx] == mx:
        print(mx, a[idx-1], sep=" ")
        exit()
    if idx > 0:
        if abs(mx//2 - (mx-a[idx])) > abs(mx//2 - a[idx-1]):
            print(mx, a[idx-1], sep=" ")
        else:
            print(mx, a[idx], sep=" ")
    else:
        print(mx, a[idx], sep=" ")
            
