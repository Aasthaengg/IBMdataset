from collections import deque
 
n = int(input())
 
def dfs(n):
  stack = deque()
  stack.append("a")
  while stack:
    q = stack.popleft()
    if len(q) == n:
      ans.append(q) 
    if len(q) < n:
      for i in range(ord("a"), ord(max(q)) + 2):
        stack.append(q + chr(i))
    #print(stack)
    
ans = []
dfs(n)
 
print("\n".join(ans))