N = int(input())
S = list(input())

R = S.count('R')
B = S.count('B')
if R > B:
  print ('Yes')
else:
  print ('No')