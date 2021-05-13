import sys
N = int(input())
s = input()
if N%2 ==1:
  print('No')
  sys.exit()
if s[:N//2] == s[N//2:]:
  print('Yes')
else:
  print('No')