n = int(input())
a = map(int, input().split())

m = 0
ans = []
for i in a:
  if i < 0:
    m += 1
    ans.append(abs(i))
  else:
    ans.append(i)
if m % 2 == 0:
  print(sum(ans))
else:
  x = min(ans)
  print(sum(ans)-x*2)