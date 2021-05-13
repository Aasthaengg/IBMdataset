a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for i in range(a,-1,-1):
  if x - 500*i < 0: continue
  for j in range(b,-1,-1):
    if x - 500*i - 100*j < 0: continue
    for k in range(c,-1,-1):
      if x - 500*i - 100*j - 50*k == 0: ans += 1
print(ans)