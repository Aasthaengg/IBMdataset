S=input()
def dfs(s,i):
  if i==len(S)-1:
    return sum(map(int,s.split("+")))
  return dfs(s+S[i+1],i+1)+dfs(s+"+"+S[i+1],i+1)
print(dfs(S[0],0))