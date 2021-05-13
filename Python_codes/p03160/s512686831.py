import sys
sys.setrecursionlimit(1001000)

N = int(input())
height = list(map(int, input().split()))

minimum_jump = [-1]*N
minimum_jump[0] = 0
minimum_jump[1] = abs(height[0] - height[1])

def frog_jump(n): #n is index of stone
  if minimum_jump[n] != -1:
    return minimum_jump[n]
  else:
    if minimum_jump[n-1] != -1:
      temp1 = minimum_jump[n-1]
    else:
      temp1 = frog_jump(n-1)
    if minimum_jump[n-2] != -1:
      temp2 = minimum_jump[n-2]
    else:
      temp2 = frog_jump(n-2)
    minimum_jump[n] = min(temp1+abs(height[n] - height[n-1]), temp2+abs(height[n] - height[n-2]))
    return minimum_jump[n]
  
print(frog_jump(N-1))