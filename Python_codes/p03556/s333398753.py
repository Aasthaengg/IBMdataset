n = int(input())
ans = 1
for num in range(n+1):
  if num*num <= n:
    ans = num*num
  else: 
    break
print(ans)