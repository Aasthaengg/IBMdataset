A, B = map(int, input().split())
S = str(input())

if (S[:A].isdecimal()) and (S[A]=='-') and (S[A+1:].isdecimal()):
  print('Yes')
else:
  print('No')