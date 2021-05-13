n=int(input())

abc='abcdefghijklmnopqrstuvwxyz'

def dfs(keta,s):
  if keta==n:
    global ans
    ans.append(s)
    return

  st_l=len(set(s))
  for i in range(st_l+1):
    dfs(keta+1,s+abc[i])

ans=[]
dfs(1,'a')

for i in ans:
  print(i)