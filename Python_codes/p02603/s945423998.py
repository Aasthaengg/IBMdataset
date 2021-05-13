n = int(input())
arr = list(map(int,input().split()))
cache = 1000
numStock = 0
for i in range(1,n):
    if arr[i]>arr[i-1]:
        available = cache//arr[i-1]
        cache -= arr[i-1]*available
        numStock += available
    else:
        cache += arr[i-1]*numStock
        numStock = 0

if numStock>0:
    cache += arr[-1]*numStock

print(cache)
