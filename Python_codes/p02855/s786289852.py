h,w,k=map(int,input().split())
s=[]
for i in range(h):
  s.append(input())
ans=[]
for i in range(h):
  ans.append([])
  for j in range(w):
    ans[-1].append(0)
flag=0
current=1
for i in range(h):
  count=0
  for j in range(w):
    if s[i][j]=='#':
      count+=1
  if count==0:
    if flag==1:
      for j in range(w):
        ans[i][j]=ans[i-1][j]
  else:
    if count==1:
      for j in range(w):
        ans[i][j]=str(current)
      current+=1
      if flag==0:
        for i2 in range(i):
          for j in range(w):
            ans[i2][j]=ans[i][j]
        flag=1
    else:
      start=0
      count2=0
      for j in range(w):
        if s[i][j]=='#':
          count2+=1
          for j2 in range(start,j+1):
            ans[i][j2]=str(current)
          if count2==count:
            for j2 in range(j+1,w):
              ans[i][j2]=str(current)
          current+=1
          start=j+1
      if flag==0:
        for i2 in range(i):
          for j in range(w):
            ans[i2][j]=ans[i][j]
        flag=1
for i in range(h):
  print(' '.join(ans[i]))