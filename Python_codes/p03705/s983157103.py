N,A,B = map(int,input().split())

if A >B:
  ans = 0
elif N==1:
  if A ==B:
    ans = 1
  else:
    ans =0
else:
  X = A*(N-1)+B
  Y = A+(N-1)*B
  ans =Y - X + 1
print(ans)