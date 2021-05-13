import math
n = int(input())
a = list(map(int,input().split()))

a = sorted(a, reverse = True)
mid = a[0]//2
diff = abs(mid - a[0])

if n == 2:
    print(max(a[0],a[1]),min(a[0],a[1]))
else:
    for i in range(n):
        if abs(a[i] - mid) < diff:
            diff = abs(a[i] - mid)
            ans = i
    print(a[0], a[ans])