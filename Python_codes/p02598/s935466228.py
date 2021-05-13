n, k = map(int, input().split())
log = list(map(int, input().split()))

left = 0
right = 10**9

while right - left > 1:
  
  mid = (left + right) // 2
  
  cut = 0
  for i in range(n):
    cut += -(log[i]//-mid)-1

  if cut > k:
    left = mid
  else:
    right = mid
    
print(right)