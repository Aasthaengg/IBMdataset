n = int(input())
a, b, c = input(), input(), input()
ans = 0
for i in range(n):
  if not a[i]==b[i]==c[i]:
    if (a[i]==b[i] and b[i]!=c[i]) or (b[i]==c[i] and c[i]!=a[i]) or (c[i]==a[i] and a[i]!=b[i]):
      ans += 1
    else:
      ans += 2
print(ans)