n = int(input())
s = input()
if n%2==1:
  print('No')
else:
  m = n//2
  print('Yes' if s[:m]==s[m:] else 'No')