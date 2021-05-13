h,w=map(int,input().split())
l=[list(map(int,input().split())) for i in range(h)]

ans_num=0
ans_l=[]
for i in range(h):
  for j in range(w):
    if j!=w-1:
      if l[i][j]%2==1:
        l[i][j]-=1
        l[i][j+1]+=1
        ans_num+=1
        ans_l.append([i+1,j+1,i+1,j+1+1])
    elif i!=h-1:
      if l[i][j]%2==1:
        l[i][j]-=1
        l[i+1][j]+=1
        ans_num+=1
        ans_l.append([i+1,j+1,i+1+1,j+1])


print(ans_num)
for i in ans_l:
  print(*i)