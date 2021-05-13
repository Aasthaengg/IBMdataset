H,W = map(int,input().split())
N = int(input())
a = [i for i in map(int,input().split())]

ans = [[0 for i in range(W)] for j in range(H)]
x=0
y=0
color=0
reverse=0

while y<H:
  ans[y][x] = color+1
  a[color]-=1
  if a[color]==0:
    color+=1
  if (reverse==0 and x==W-1) or (reverse==1 and x==0):
    reverse = 1-reverse
    y+=1
  else:
    if reverse==0:
      x+=1
    else:
      x-=1
    
for i in range(H):
  print(" ".join(map(str,ans[i])))