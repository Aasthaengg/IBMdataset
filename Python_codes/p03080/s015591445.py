n = int(input())
s = input()

R = s.count('R')
B = len(s)-R

if R > B:
  print('Yes')
else:
  print('No')
