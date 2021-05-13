n = int(input())
ds = list(map(int, input().split()))
ds.sort()
n_f = n//2-1
n_b = n//2
print(ds[n_b]-ds[n_f])