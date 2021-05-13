X = int(input())
ans = 10 ** 9
for i in range(1,32):
  for j in range(2,10):
    if i ** j <= X: ans = min(ans,X -  i ** j)
print(X - ans)      