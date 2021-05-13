n = int(input())
ans = 1
b = 0
if n < 105:
  print(0)
elif n == 105:
  print(1)
else:
  for i in range(106,n+1):
    b = 0
    for j in range(1, i+1,2):
      if i % j ==0:
        b +=1
    if b == 8:
      ans += 1
  print(ans)