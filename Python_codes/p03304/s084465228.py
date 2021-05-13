a = list(map(int, input().split()))
if a[2] == 0:
    print(1.0 * (a[1] - 1) / a[0])
else:
    print(2.0 * (a[0] - a[2]) / a[0] / a[0] * (a[1] - 1))
