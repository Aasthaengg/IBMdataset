n = int(input())
a,b = map(int, input().split())
res = [0,0,0]
arr = list(map(int, input().split()))
for i in range(n):
  if arr[i] <= a:
    res[0] += 1
  elif arr[i] <= b:
    res[1] += 1
  else:
    res[2] += 1
print(min(res))
