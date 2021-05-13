A = input()
B = input()
ans = ''
if len(A) < len(B):
  ans = 'LESS'
elif len(A) > len(B):
  ans = 'GREATER'
elif len(A) == len(B):
  for i in range(len(A)):
    if int(A[i]) > int(B[i]):
      ans = 'GREATER'
      break;
    elif int(B[i]) > int(A[i]):
      ans = 'LESS'
      break;
    if i == len(A)-1:
      if int(B[i]) == int(A[i]):
        ans = 'EQUAL'
print(ans)