N = int(input())
ds = list(map(int, input().split()))

ds.sort()

d_miman = ds[N // 2 -1]
d_ijyou = ds[N // 2]

print(d_ijyou - d_miman)