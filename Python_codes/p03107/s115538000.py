S = list(input())
a = 0
b = 0
for s in S:
  if s == '0':
    a += 1
  else:
    b += 1
ans = min(a,b)
ans = ans * 2
print(ans)