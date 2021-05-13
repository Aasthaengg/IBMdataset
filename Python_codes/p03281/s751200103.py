n = int(input())
ans = 0

for i in range(1, n+1):
  counter = 0
  
  if i%2==0:
    continue
  
  for i_i in range(1, i+1):
    if i%i_i == 0:
      counter += 1
  
  if counter == 8:
    ans += 1
    
print(ans)