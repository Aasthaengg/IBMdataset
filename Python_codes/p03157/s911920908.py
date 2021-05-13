from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from collections import deque

h,w=nii()
s=[list(input()) for i in range(h)]

def BFS(sy,sx,ans):
  s[sy][sx]='B'

  que=deque()
  que.append((sy,sx))

  b_cnt=1
  w_cnt=0

  while que:
    y,x=que.popleft()
    for dy,dx in [[-1,0],[0,-1],[1,0],[0,1]]:
      ny=y+dy
      nx=x+dx
      if 0<=ny<h and 0<=nx<w:
        if s[y][x]=='B' and s[ny][nx]=='.':
          w_cnt+=1
          s[ny][nx]='W'
          que.append((ny,nx))
        if s[y][x]=='W' and s[ny][nx]=='#':
          b_cnt+=1
          s[ny][nx]='B'
          que.append((ny,nx))

  ans+=b_cnt*w_cnt
  return ans

ans=0
for i in range(h):
  for j in range(w):
    if s[i][j]=='#':
      ans=BFS(i,j,ans)

print(ans)
