n = int(input())
k = int(input())
ans = 1
for i in range(n):
  a = ans * 2
  b = ans + k
  if a < b:
    ans = a
  else:
    ans = b
print(ans)
