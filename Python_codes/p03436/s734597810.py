h,w=map(int, input().split())
s=[list(input()) for i in range(h)]

blackCnt=0
for i in s:
  for j in i:
    if j=="#":
      blackCnt+=1


#スタートをキューに格納
q=[[0,0]]
route=[[1,0],[0,1],[-1,0],[0,-1]]
visited = [[0 for i in range(w)] for j in range(h)]
visited[0][0]=1
cnt=0
while q:
  
  for _ in range(len(q)):
    x,y = q.pop(0)
    
    for i in range(4):
      nx, ny = x+route[i][0], y+route[i][1]
      #条件に合致すれば追加
      if 0<=nx<h and 0<=ny<w and visited[nx][ny] == 0 and s[nx][ny] != '#':
        q.append([nx,ny])
        visited[nx][ny]=1
  cnt+=1
  if visited[h-1][w-1]==1:
    print(w*h-cnt-1-blackCnt)
    exit()
print(-1)