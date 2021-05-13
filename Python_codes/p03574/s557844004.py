import copy
h,w=map(int, input().split())
s=[list(input())  for i in  range(h)]
ans=copy.deepcopy(s)

around=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

for i in range(h):
  for j in range(w):
    x,y=i,j
    if s[x][y]==".":
      cnt=0
      for a in around:
        if (x+a[0]<0 or x+a[0]>h-1) or (y+a[1]<0 or y+a[1]>w-1):
          continue
        if s[x+a[0]][y+a[1]]=="#":
          cnt+=1
      ans[x][y]=str(cnt)
    

for i in ans:
  print("".join(i))
