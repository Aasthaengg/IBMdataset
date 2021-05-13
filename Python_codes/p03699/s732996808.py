n = int(input())
s = [0]*n

for i in range(n):
  s[i] = int(input())
  
s.sort()

if sum(s)%10 != 0:
  print(sum(s))
else:
  i = 0
  ss = sum(s)
  for i in range(n):
    if s[i]%10 != 0:
      print(ss-s[i])
      exit()
  print(0)