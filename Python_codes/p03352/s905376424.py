x = int(input())

ans = []
if x == 1:
  print(1)
  exit()

for i in range(2,x+1):
  for j in range(2,x+1):
    if i**j > x:
      break
    ans.append(i**j)

if len(ans)==0:
  print(0)
else:
  print(max(ans))