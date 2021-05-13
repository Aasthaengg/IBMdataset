S = input()
T = S.replace('BC', 'X')

ans = 0
cnta = 0
for ch in T:
  if ch == 'B' or ch == 'C':
    cnta = 0
  elif ch == 'A':
    cnta += 1
  else:
    ans += cnta
    
print(ans)