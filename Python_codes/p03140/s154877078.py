n = int(input())
a = input()
b = input()
c = input()
ans = 0
for i in range(n):
  if a[i].count(b[i]) + b[i].count(c[i]) + c[i].count(a[i]) != 3:
    ans += 2 - (a[i].count(b[i]) + b[i].count(c[i]) + c[i].count(a[i]))
print(ans)