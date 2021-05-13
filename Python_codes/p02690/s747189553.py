X = int(input())

check = False
for i in range(-118,120):
  for j in range(-118,120):
    if i ** 5 - j ** 5 == X:
      ans = [i,j]
      check = True
      break
  if check:
    break
    
print(*ans)