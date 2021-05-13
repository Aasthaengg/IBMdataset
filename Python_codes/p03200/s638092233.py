S = input()
B_count = 0
ans = 0
for c in S:
  if c == 'B':
    B_count += 1
  elif c == 'W':
    ans += B_count
print(ans)