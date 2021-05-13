a = []
for i in range(3):
  a.append(input())
ans = ""
for i in range(3):
  ans += a[i][i]

print(ans)