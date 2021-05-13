n = str(input())

ans = 0
for i in range(len(n)):
  ans += int(n[i])
  
if ans == 1:
  print(10)
else:
  print(ans)