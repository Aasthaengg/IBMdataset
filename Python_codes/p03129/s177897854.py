

n,k = map(int,input().strip().split(' '))
c = 0
for i in range(n):
  if i%2 == 0:
    c+=1
if(c>=k):
  print("YES")
else:
  print("NO")