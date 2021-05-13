import numpy as np

def dfs(A, a, n, ans):
  if len(A) == n:
    tmp = np.array(A) + a
    if sum(tmp % 2) < len(A):
      ans += 1
    return ans
  
  for i in range(-1, 2):
    A.append(i)
    ans = dfs(A, a, n, ans)
    A.pop()
    
  return ans

n = int(input())
a = np.array(list(map(int, input().split())))

print(dfs([], a, n, 0))