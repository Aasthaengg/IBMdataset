s = input()
k = int(input())


def dfs(sub, i):
  if sub in s:
    i += 1
    if i == k:
      print(sub)
      exit()
    for c in range(ord('a'), ord('z') + 1):
      c = chr(c)
      i = dfs(sub + c, i)
  return i
  
dfs('', -1)