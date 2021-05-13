n = int(input())
s = input()
a = (len(s)//2)
count = 0
if n % 2 == 0:
  for i in range (a):
    if s[i] == s[a + i]:
      count += 1
  if count == n/2:
    print('Yes')
  else:
    print('No')
else: 
  print('No')
