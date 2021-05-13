N = input()
n = len(N)

if n == 1:
  print(N)
elif N[1:] == '9'*(n-1):
  print(9*(n-1)+int(N[0]))
else:
  print(9*(n-1)+int(N[0])-1)