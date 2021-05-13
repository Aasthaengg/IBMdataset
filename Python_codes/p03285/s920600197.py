n = int(input())
maxnum_4 = n // 4
maxnum_7 = n // 7
ans = 'No'
for i in range(maxnum_7 + 1):
  for j in range(maxnum_4 + 1):
    total = i * 7 + j * 4
    if total == n:
      ans = 'Yes'
      break
  if ans == 'Yes':
    break
print(ans)