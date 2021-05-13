s = input()
k = int((len(s) -1)/2) 
l = int((len(s) + 3)/2) - 1
n = list(s)
if n[0:k] == n[l:]:
  print('Yes')
else:
  print('No')