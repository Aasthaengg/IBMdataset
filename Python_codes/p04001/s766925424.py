def dfs(i,s):
  if i == n-1:
    return eval(s)

  return dfs(i+1, s+S[i+1]) + \
         dfs(i+1, s+"+"+S[i+1])

S = str(input())
n = len(S)

print(dfs(0,S[0]))