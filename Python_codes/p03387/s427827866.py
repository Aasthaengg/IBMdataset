a = list(map(int, input().split()))
a.sort()
ans = a[2]-a[1]
a[0] += ans
if (a[2]-a[0])%2 == 0:
    print(ans+(a[2]-a[0])//2)
else:
    print(ans+(a[2]-a[0])//2+2)
