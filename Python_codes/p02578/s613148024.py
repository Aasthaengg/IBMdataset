N = int(input())
arr = list(map(int, input().split(" ")))

result = 0
p = arr[0]

for i in range(1, len(arr)):
  if p >= arr[i]:
    result += p - arr[i]
  else:
    p = arr[i]

print(result)