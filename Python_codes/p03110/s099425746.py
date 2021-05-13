n = int(input())
xu = [input().split() for i in range(n)]
y = 0
b = 0
for j in xu:
  if j[1] == "JPY":
    y += int(j[0])
  else:
    b += float(j[0])
ans = y + 380000 * b
print(ans)