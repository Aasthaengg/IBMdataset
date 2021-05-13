n, k = [int(x) for x in input().split()]
ans = 0
for i in range(n):
  if i == 0:
  	ans = k
  else:
    ans *= k-1
print(ans)