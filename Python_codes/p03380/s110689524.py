N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

x = a[0] // 2
l = 1
r = N - 1
while r - l > 1:
    mid = l + (r - l) // 2
    if a[mid] < x:
        r = mid
    else:
        l = mid
if abs(x - a[l]) <= abs(x - a[r]):
    print(a[0], a[l])
else:
    print(a[0], a[r])
