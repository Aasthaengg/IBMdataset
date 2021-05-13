n=int(input())
m=-1
for i in range(2,10**5):
  if n==i*(i-1)//2:
    m=i
    break
if m==-1:print("No");exit()
print("Yes")
ans=[[]for _ in range(m)]
for i in range(m-1):
  if i==0:x=1
  else:x=ans[0][i]
  for j in range(m-1):
    ans[i].append(x)
    if i<=j:x+=j+1
    else:x+=1
x=1
for j in range(m-1):
  ans[-1].append(x)
  x+=j+2
print(m)
for i in ans:
  print(m-1,end=" ")
  print(*i)