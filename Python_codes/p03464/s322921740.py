N = int(input())
A = list(map(int, input().split()))

B = [(0, 0)] * (N + 1)
B[N] = (2, 2)

for i in range(N - 1, -1, -1):
  min_next, max_next = B[i + 1]
  
  min_left = -1
  min_right = 10 ** 15
  
  while min_left + 1 < min_right:
    min_mid = (min_left + min_right) // 2
    mid_next = min_mid // A[i] * A[i]
    if mid_next >= min_next:
      min_right = min_mid
    else:
      min_left = min_mid
  
  max_left = 0
  max_right = 10 ** 15
  
  while max_left + 1 < max_right:
    max_mid = (max_left + max_right) // 2
    mid_next = max_mid // A[i] * A[i]
    if mid_next >= max_next + 1:
      max_right = max_mid
    else:
      max_left = max_mid
  
  if  min_right == 0 or max_left == 0 or max_left < min_right:
    print(-1)
    exit()
  else:
    B[i] = (min_right, max_left)

print(*B[0])