import collections

h,w=map(int,input().split())
color=[[0]*w for _ in range(h)]
for i in range(h):
  s=input()
  for j in range(w):
    if s[j]=='#':
      color[i][j]=1
used=[[0]*400 for _ in range(400)]
ans=0
bc=0
wc=0
for i in range(0,h):
  for j in range(0,w):
    if used[i][j]==1:
      continue
    bc=0
    wc=0
    q=collections.deque()
    used[i][j]=1
    q.append([i,j])
    while 1:
      if len(q)==0:
        break
      else:
        ti,tj=q.popleft()
        if color[ti][tj]==1:
          bc+=1
        else:
          wc+=1
        if ti-1>=0:
          if color[ti][tj]!=color[ti-1][tj]:
            if used[ti-1][tj]==0:
              used[ti-1][tj]=1
              q.append([ti-1,tj])
        if ti+1<=h-1:
          if color[ti][tj]!=color[ti+1][tj]:
            if used[ti+1][tj]==0:
              used[ti+1][tj]=1
              q.append([ti+1,tj])
        if tj-1>=0:
          if color[ti][tj]!=color[ti][tj-1]:
            if used[ti][tj-1]==0:
              used[ti][tj-1]=1
              q.append([ti,tj-1])
        if tj+1<=w-1:
          if color[ti][tj]!=color[ti][tj+1]:
            if used[ti][tj+1]==0:
              used[ti][tj+1]=1
              q.append([ti,tj+1])
    ans+=bc*wc
print(ans)