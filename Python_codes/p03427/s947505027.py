S = list(input())
S = list(map(lambda x: int(x),S))
ans = 0

for i in range(len(S) - 1,0,-1):
  
  if S[i] == 9:
    tmp = sum(S)
  else:
    S[i] = 9
    S[i - 1] -= 1
    tmp = sum(S)
  
  ans = max(tmp,ans)

if len(S) == 1:
  ans = S[0]

print(ans)