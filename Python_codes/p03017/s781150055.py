N, A, B, C, D = map(int, input().split())
S = str(input())

flag = True
if C < D:
  for i in range(A, D-2):
    if (S[i]=='#') and (S[i+1]=='#'):
      flag = False
      break
else:
  for i in range(A, C-2):
    if (S[i]=='#') and (S[i+1]=='#'):
      flag = False
      break
  if flag:
    flag = False
    for i in range(B-1, D):
      if (S[i-1]=='.') and (S[i]=='.') and (S[i+1]=='.'):
        flag = True
        break
        
if flag:
  print('Yes')
else:
  print('No')