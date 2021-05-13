n = int(input())

s = 0
for i in range(1,10**5):
  s += i
  if s >= n:
    t = i
    break

if s == n:
  for i in range(1,t+1):
    print (i)
else:
  for i in range(1,t+1):
    if i == s-n:
      continue
    print (i)
exit()