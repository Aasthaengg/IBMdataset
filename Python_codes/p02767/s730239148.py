import math
n = input()
arr = list(map(int, input().split()))
a = sum(arr) // len(arr)
b = a + 1
'''
arr.sort()
if len(arr) % 2 == 0:
    mid = len(arr) // 2
    avg = (arr[mid] + arr[mid-1]) // 2
else:
    mid = len(arr) // 2
    avg = arr[mid]

print(avg)
'''
ans = 0
ans2 = 0
for p in arr:
    ans += (a - p)**2
    ans2  += (b - p)**2
print(min(ans, ans2))
