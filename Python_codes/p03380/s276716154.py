n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
amax = a[0]
na = a[1:]
d = {}
for el in na:
    d[el] = abs(el - amax//2)
ds = sorted(d.items(), key=lambda x:x[1])
print(amax, ds[0][0])