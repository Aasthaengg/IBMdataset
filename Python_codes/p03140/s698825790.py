n = int(input())
a = input()
b = input()
c = input()
ans = 0
for i in range(n):
  if (a[i] == b[i]) & (b[i] == c[i]):
    continue
  if (a[i] == b[i]) | (b[i] == c[i]) | (c[i] == a[i]):
    ans += 1
    continue
  ans += 2
print(ans)
