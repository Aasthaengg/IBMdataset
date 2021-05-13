N,A,B,C,D = map(int,input().split())
S = list(input())

ans = 'Yes'
if (C < D):
  for i in range(B-1,D-1):
    if (S[i] == '#' and S[i+1] == '#'):
      ans = 'No'
      break
  for i in range(A-1,C-1):
    if (S[i] == '#' and S[i+1] == '#'):
      ans = 'No'
      break
else:
  can_over = False
  for i in range(A-1,C-1):
    if (S[i] == '#' and S[i+1] == '#'):
      ans = 'No'
      break
    
  for i in range(B-1,D):
    if (S[i-1] == '.' and S[i] == '.' and S[i+1] == '.'):
      can_over = True
  if (can_over == False):
    ans = 'No'
print(ans)