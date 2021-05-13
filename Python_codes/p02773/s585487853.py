N=int(input())
d={}
ans=[]
num=0
for x in range(N):
  S=input()
  if S not in d:
    d[S]=1
  else:
    d[S] += 1
  if d[S]>num:
    num=d[S]
    ans=[]
    ans.append(S)
  elif d[S]==num:
    ans.append(S)
ans.sort()
for i in range(len(ans)):
  print(ans[i])
    
