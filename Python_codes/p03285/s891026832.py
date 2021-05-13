n = int(input())

ans = 'No'
for i4 in range(26):
  for i7 in range(15):
    if i4*4 + i7 *7 - n == 0:
      ans = 'Yes'
      break
    else:
      continue

print(ans)