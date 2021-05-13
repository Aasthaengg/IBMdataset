n = int(input())
res = "No"
for i in range(1,10):
  for j in range(1,10):
    if i*j == n:
      res = "Yes"
print(res)