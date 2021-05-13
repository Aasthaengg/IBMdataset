n, x = map(int, input().split())
a = list(map(int, input().split()))
num = len(a)


ans = 0

for i in range(num - 1):
    tar = a[i] + a[i + 1]
    if (tar <= x):
        continue
    else:
        dif = tar - x
        if (a[i + 1] >= dif):
            ans += dif
            a[i + 1] -= dif

        else:
            ans += a[i + 1]
            dif -= a[i + 1]
            a[i + 1] = 0

            a[i] -= dif
            ans += dif


print(ans)
