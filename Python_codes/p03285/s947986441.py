n = int(input())

def dfs(x):
  if x > n: return
  if x == n: print("Yes"), exit(0)
  dfs(x + 4)
  dfs(x + 7)

dfs(0)
print("No")