n = int(input())
min_val, max_val = zip(*[map(int, input().split()) for _ in range(n)])
min_val = sorted(min_val)
max_val = sorted(max_val)

if n % 2:
    mid = n//2
    min_median = min_val[mid]
    max_median = max_val[mid]
    print(max_median-min_median+1)
else:
    midl = (n-1)//2
    midr = midl+1
    min_median = min_val[midl]+min_val[midr]
    max_median = max_val[midl]+max_val[midr]
    print(max_median-min_median+1)
