x = input()
y = input()
ans = 0
for i in range(len(x)):
  for j in range(len(y)):
    if i == j:
      if x[i] == y[j]:
        ans += 1
print(ans)
