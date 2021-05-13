a = list(input())
b = list(input())
 
a.sort()
b.sort(reverse=True)
if ''.join(a) < ''.join(b):
  print('Yes')
else:
  print('No')