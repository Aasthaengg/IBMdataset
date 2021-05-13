N = int(input())
L = list(map(int, input().split()))
L.sort()
def find(arr, x):
  if arr[0] >= x:
    return 0
  if arr[-1] < x:
    return len(arr)
  
  l = 0
  h = len(arr)
  
  while h - l > 1:
    m = (l+h) // 2
    if arr[m] < x:
      l = m
    else:
      h = m
  return h

ans = 0

for i in range(N-2):
  for j in range(i+1, N-1):
    x = L[i] + L[j]
    temp = find(L[j+1:], x)
    ans += temp
print(ans)