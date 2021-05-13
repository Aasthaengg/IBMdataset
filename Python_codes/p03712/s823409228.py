H,W=map(int,input().split())
ans=[["#"]*(W+2) for i in range(H+2)]
for y in range(H):
  a=input()
  for x in range(len(a)):
    ans[y+1][x+1]=a[x]
for y in range(H+2):
  for x in range(W+2):
    print(ans[y][x],end="")
  print()
