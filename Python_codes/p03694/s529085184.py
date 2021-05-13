n = int(input())
arr = list(map(int, input().split()))
arr.sort()
k = 0
for i in range(len(arr) - 1):
  k += arr[i + 1] - arr[i]
print(k)