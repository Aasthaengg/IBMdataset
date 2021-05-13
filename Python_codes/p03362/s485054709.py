n = int(input())
prime5 = []
for i in range(1,5600):
  a = i * 10 + 1
  # flag = True
  for j in range(3,int(a**0.5) + 1):
    if a % j == 0:
      break
      # flag = False
  else: prime5.append(a)
print(*prime5[:n])
