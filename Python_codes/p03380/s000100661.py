n=int(input())
a=list(map(int, input().split()))

a.sort(reverse=True)
ideal = a[0]//2
dif_mn = 10**9

for i in range(1,n):
    tmp = a[0]-a[i] if a[i] > ideal else a[i]
    dif = ideal-tmp
    if dif < dif_mn:
        r = a[i]
        dif_mn = dif

print(a[0], r)
