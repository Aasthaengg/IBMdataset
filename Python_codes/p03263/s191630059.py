H,W=map(int,input().split())
N=0
L= [list(map(int,input().split(" "))) for i in range(H)]
ans1=list()
ans2=list()
ans3=list()
ans4=list()
for i in range(H):
  for j in range(W):
    if i==H-1:
      if j==W-1:
        break
      else:
        for k in range(L[i][j]%2):
          ans1.append(i+1)
          ans2.append(j+1)
          ans3.append(i+1)
          ans4.append(j+2)
        L[i][j+1]+=L[i][j]%2
        N+=L[i][j]%2
    else:
      for k in range(L[i][j]%2):
        ans1.append(i+1)
        ans2.append(j+1)
        ans3.append(i+2)
        ans4.append(j+1)
      L[i+1][j]+=L[i][j]%2
      N+=L[i][j]%2
print(N)
for i in range(N):
  print(ans1[i],ans2[i],ans3[i],ans4[i])