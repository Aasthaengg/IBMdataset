S = list(str(input()))
T = list(str(input()))
ans = 'No'
if S == T:
  ans = 'Yes'
else:
  for i in range(len(T)):
    s = S.pop()
    S = [s] + S
    if S == T:
      ans = 'Yes'

print(ans)