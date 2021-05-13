n, k = map(int, input().split())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
arr.sort()
s = 0
for i in range(n):
    s+=arr[i][1]
    if s >= k:
        print(arr[i][0])
        exit()
print(arr[-1][0])
