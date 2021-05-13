n = int(input())

ans = 0
for i in range(1, n):
  tmp = n - i
  if i < tmp:
    ans  += 1
    
print(ans)