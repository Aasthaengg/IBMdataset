A = list(input())
A = set(A)

x = 0
for c in 'abcdefghijklmnopqrstuvwxyz':
  if c not in A:
    print(c)
    x = 1
    break
if x == 0:
  print('None')