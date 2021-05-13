S = input()

p = 0
ans = 0

for i, c in enumerate(S):
  if c == 'B':
    continue
  ans += (i - p)
  p += 1
  
print(ans)