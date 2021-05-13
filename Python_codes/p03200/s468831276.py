S = input()
w = 0
ans = 0
for i, s in enumerate(S):
  if s == 'W':
    ans += i - w
    w += 1
    
print(ans)