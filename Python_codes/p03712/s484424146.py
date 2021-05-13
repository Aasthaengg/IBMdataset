h,w=map(int,input().split())
S=[list(input()) for i in range(h)]
for i in range(h+2):
  for j in range(w+2):
    if i in [0,h+1] or j in [0,w+1]:
      print("#",end="")
    else:
      print(S[i-1][j-1],end="")
  print("")