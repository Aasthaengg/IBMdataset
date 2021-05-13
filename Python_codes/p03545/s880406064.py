s = input()
n = len(s)


for i in range(2**(n-1)):
  ans = int(s[0])
  f = s[0]
  for j in range(n-1):
    if i & (1<<j):
      f += '+'
      ans += int(s[j+1])
    else:
      f += '-'
      ans -= int(s[j+1])
    f += s[j+1]
    
  if ans == 7:
    print(f + '=7')
    exit()