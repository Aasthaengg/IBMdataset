N = int(input())
ds = list(map(int,input().split()))
ds.sort()
c1 = ds[N//2-1]
c2 = ds[N//2]
print(c2-c1)