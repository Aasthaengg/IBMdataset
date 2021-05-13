N, K = map(int, input().split())
height = list(map(int,input().split()))
min_jump = [0,abs(height[0]-height[1])]

for num in range(2,N): #num is index of stone
  jump = 10**9
  if num < K:
    for n in range(num): # n is number of passed stones
      jump = min(jump, min_jump[num-n-1] + abs(height[num-n-1] - height[num]))
    min_jump.append(jump)
  else:
    for n in range(K): # n is number of passed stones
      jump = min(jump, min_jump[num-n-1] + abs(height[num-n-1] - height[num]))
    min_jump.append(jump)
print(min_jump[N-1])
