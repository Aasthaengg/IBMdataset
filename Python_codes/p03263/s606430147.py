h,w=map(int,input().split())
a=[]
for i in range(h):
  a.append(list(map(int,input().split())))
carry=0
ans=[]
for i in range(h):
  for j in range(w-1):
    if i%2==0:
      if (carry+a[i][j])%2==1:
        ans.append([i+1,j+1,i+1,j+2])
        carry=1
      else:
        carry=0
    if i%2==1:
      if (carry+a[i][w-1-j])%2==1:
        ans.append([i+1,w-j,i+1,w-1-j])
        carry=1
      else:
        carry=0
  if i%2==0 and i!=h-1:
    if (carry+a[i][w-1])%2==1:
      ans.append([i+1,w,i+2,w])
      carry=1
    else:
      carry=0
  if i%2==1 and i!=h-1:
    if (carry+a[i][0])%2==1:
      ans.append([i+1,1,i+2,1])
      carry=1
    else:
      carry=0
print(len(ans))
for b in ans:
  t=[]
  for i in b:
    t.append(str(i))
  print(' '.join(t))
