h,w=map(int,input().split())
S=[list(input()) for i in range(h)]
ans= [["" for i in range(w)] for j in range(h)]
for i in range(h):
  for j in range(w):
    if S[i][j]=="#":
      ans[i][j]="#"
    else:
      cnt = 0
      for k in range(-1,2):
        for l in range(-1,2):
          if 0<=i+k<h and 0<=j+l<w and S[i+k][j+l]=="#":
            cnt += 1
      ans[i][j]=str(cnt)
for i in range(h):
  for j in range(w):
    print(ans[i][j],end="")
  print("")
