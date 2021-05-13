a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
for i in range(a+1):
  if i * 500 == x:
    ans += 1
    break
  for j in range(b+1):
    if i * 500 + j * 100 == x:
      ans += 1
      break
    for k in range(c+1):
      if i * 500 + j * 100 + k * 50 == x:
        ans += 1
        break
print(ans)