Y_DIR=[-1,0,1]
X_DIR=[-1,0,1]
def count_bomb(y,x):
  cnt=0
  for yd in Y_DIR:
    yy=y+yd
    if not (0<=yy<h):
      continue
    for xd in X_DIR:
      xx=x+xd
      if not (0<=xx<w):
        continue
      if s[yy][xx]=="#":
        cnt+=1
  return cnt

h,w=map(int,input().split())
s=[]
for i in range(h):
  s.append(input())
  
ans=["" for _ in range(h)]
for y in range(h):
  for x in range(w):
    if s[y][x] == ".":
      c=count_bomb(y,x)
      ans[y]+=str(c)
    else:
      ans[y]+=s[y][x]

print("\n".join(ans)) 
      
