S = str(input());T = str(input())
N = len(S)
M = len(T)
ans = M
for i in range(N-M+1):
  kouho = S[i:i+M]
  temp = 0
  #print(kouho,T)
  for j in range(M):
    if kouho[j] != T[j]:
      temp += 1
  ans = min(ans,temp)
print(ans)