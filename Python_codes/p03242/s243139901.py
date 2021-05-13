S = list(input())
for i in range(3):
  if S[i] == '1':
  	S[i] = '9'
  elif S[i]== '9':
    S[i] = '1'
A = int(''.join(S))
print(A)