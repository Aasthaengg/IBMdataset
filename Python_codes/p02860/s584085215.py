n = int(input())
t = input()
if n % 2 != 0:
  print('No')
else:
  print('Yes' if t[:n//2] == t[n//2:] else 'No')
