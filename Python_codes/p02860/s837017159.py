n = int(input())
s = input()

l_a = []
l_b = []

if n%2 == 0:
  for i in range(n//2):
    l_a.append(s[i])
  for i in range(n//2, n):
    l_b.append(s[i])
  if l_a == l_b:
    print('Yes')
  else:
    print('No')
else:
  print('No')