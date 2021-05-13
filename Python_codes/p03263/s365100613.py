h,w=map(int,input().split())
num=[list(map(int,input().split())) for i in range(h)]
ctrl=[]
cnt=0
for i in range(h):
  for j in range(w):
    if i==h-1:
      if j==w-1:pass
      else:
        if num[i][j]%2==1:
          num[i][j]-=1
          num[i][j+1]+=1
          ctrl.append([i+1,j+1,i+1,j+2])
          cnt+=1
    else:
      if num[i][j]%2==1:
        num[i][j]-=1
        num[i+1][j]+=1
        ctrl.append([i+1,j+1,i+2,j+1])
        cnt+=1
print(cnt)
for i in range(cnt):
  print(ctrl[i][0],ctrl[i][1],ctrl[i][2],ctrl[i][3])
