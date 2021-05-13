N = int(input())
a = [int(i) for i in input().split()]
sunuke = a[0]
arai = sum(a[1:])
if N == 2:
    print(abs(a[0] - a[1]))
else:
    ans = float('inf')
    for i in range(1, N-1):
        sunuke += a[i]
        arai -= a[i]
        ans = min(ans, abs(sunuke - arai))

    print(ans)