S = str(input())
n = len(S)

def dfs(i,f,total):
  if i == n - 1:
    if total == 7:
      print(f + '=7')
      exit()
  else:
    dfs(i+1,f + '+' + S[i+1],total + int(S[i+1]))
    dfs(i+1,f + '-' + S[i+1],total - int(S[i+1]))

dfs(0,S[0],int(S[0]))