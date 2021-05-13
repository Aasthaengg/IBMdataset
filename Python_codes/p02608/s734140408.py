N = int(input())

ans = [0] * (N+1)
for a in range(1, 105):
  if a*a > N :
    break
  for b in range(1, 105):
    if a*a + b*b > N:
      break      
    for c in range(1, 105):
      if a*a + b*b + c*c + a*b + b*c + c*a > N:
        break
      ans[a*a + b*b + c*c + a*b + b*c + c*a] += 1

for i in range(1, N+1):
  print(ans[i])
