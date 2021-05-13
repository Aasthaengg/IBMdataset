n = int(input())
arr = [int(input()) for i in range(n)]

m = 1 - 10**9
minv = arr[0]
for i in range(1,len(arr)):
    if arr[i] - minv > m:
        m = arr[i] - minv
    minv = min(minv, arr[i])
print(m)    