n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

max_a = max(a)
a.remove(max_a)
da = [abs(ai - max_a / 2) for ai in a]
med_i = da.index(min(da))

print("%d %d" % (max_a, a[med_i]))
