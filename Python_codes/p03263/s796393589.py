h,w = tuple(map(int,input().split()))

a = [[int(t)for t in input().split()]for _ in [0]*h]

steps = []
for i in range(h):
  if i%2==0:
    for j in range(w-1):
      if a[i][j]%2==1:
        steps.append((i+1,j+1,i+1,j+2))
        a[i][j+1]+=1
    if i!=h-1 and a[i][-1]%2==1:
      steps.append((i+1,w,i+2,w))
      a[i+1][-1] +=1
  else:
    for j in range(1,w)[::-1]:
      if a[i][j]%2==1:
        steps.append((i+1,j+1,i+1,j))
        a[i][j-1]+=1
    if i!=h-1 and a[i][0]%2==1:
      steps.append((i+1,1,i+2,1))
      a[i+1][0] +=1

    
print(len(steps))
for s in steps:
  print(*s)
    
      
