S = input()

cnt = 0
for c in S:
  if c == 'x':
    cnt += 1
    
print('NO' if cnt > 7 else 'YES')