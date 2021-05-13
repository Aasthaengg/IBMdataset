n = int(input())

ans = []
r = n
if n % 2 == 0:
  r = n+1
      
for i in range(n):
  for j in range(i+1,n):
    if i+j+2 == r:
      continue
    ans.append([i+1,j+1])
      
print(len(ans))
for a in ans:
  print(*a)