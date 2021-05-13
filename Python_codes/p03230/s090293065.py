def chk(k):
  if k*(k-1)//2 != n:
    return False
  l=[[] for i in range(k)];x=1
  for i in range(k):
    for j in range(i+1,k):
      l[i].append(x);l[j].append(x);x+=1
  print("Yes\n"+str(k))
  for i in range(k):
    print(len(l[i]),' '.join(map(str,l[i])))
  return True
  
n=int(input());flag=False
for i in range(1,1000):
  if chk(i):
    flag=True
    exit()
if not flag:
  print("No")