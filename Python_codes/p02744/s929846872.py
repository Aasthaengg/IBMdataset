import sys
sys.setrecursionlimit(100000000)
def dfs(s,n,m,subs):
  if len(subs)==n:
    print(subs)
    return
  
  k = len(set(list(subs)))+1

  for i in range(k):
    t = "".join((subs,s[i]))
    dfs(s,n,k,t)

s = "abcdefghij"

n = int(input())
s = list(s[:n])
dfs(s,n,1,"a")