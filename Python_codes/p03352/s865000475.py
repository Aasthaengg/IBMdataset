x = int(input())

if x ==1:
  print(1)
else:
  ans = []
  for i in range(1, x):
    for j in range(2, x//i):
      if i**j>x:
        break
      else:
        ans.append(i**j)
  
  print(max(ans))