ds = list(map(int, input().split()))
k = int(input())
ds = sorted(ds)
print(ds[0] + ds[1] + ds[2]*(2**k))