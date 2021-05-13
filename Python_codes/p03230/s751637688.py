n=int(input())
if n==1:
  print("Yes")
  print(2)
  print(1,1)
  print(1,1)
  exit()
i=1
k=-1
while i<=n:
  if n==i*(i-1)//2:
    k=i
    break
  i+=1
if k==-1:
  print("No")
  exit()
ans=[[]for _ in range(k)]
anss=1
for i in range(k-1):
  for j in range(k-i-1):
    ans[i].append(anss)
    ans[i+j+1].append(anss)
    anss+=1
print("Yes")
print(k)
for i in ans:
  print(k-1,end=" ")
  print(*i)