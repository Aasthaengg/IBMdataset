N = int(input())
S = input()

if N % 2 == 0:
  n = N // 2
  s = S[0:n]

  if S == s * 2:
    print('Yes')
  else:
    print('No')
    
else:
  print('No')