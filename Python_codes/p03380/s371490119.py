n = int(input())
a = [int(i) for i in input().split()]
max_a = max(a)
a.remove(max_a)
da = [abs(ai - max_a/2) for ai in a]
med_i = da.index(min(da))
print(max_a, a[med_i])