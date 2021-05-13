a = input()

for i in range(1 << 3):
  ans = int(a[0])
  f = a[0]
  
  for j in range(3):
    if i & (1 << j):
      ans += int(a[j+1])
      f += '+'
    else:
      ans -= int(a[j+1])
      f += '-'
    f += a[j+1]
    
  if ans == 7:
    print(f + '=7')
    exit()