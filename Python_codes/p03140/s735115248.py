n = int(input())
a = str(input())
b = str(input())
c = str(input())
ans = 0
for i in range(n):
  if a[i] == b[i] and b[i] == c[i]:
    ans += 0
  elif a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
    ans += 1
  else:
    ans += 2
print(ans)