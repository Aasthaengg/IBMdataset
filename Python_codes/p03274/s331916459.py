import bisect
N, K = [int(i) for i in input().split()]
xs = [int(i) for i in input().split()]

ans = []
bisect.insort_left(xs, 0)
for l in range(len(xs)):
    if l+K < len(xs):
        xl = xs[l]
        xr = xs[l+K]
    elif l-K > -1:
        xl = xs[l-K]
        xr = xs[l]
    else:
        continue

    tmp1 = abs(xl) + abs(xr-xl)
    tmp2 = abs(xr) + abs(xr-xl)
    ans.append(min(tmp1, tmp2))

print(min(ans))
