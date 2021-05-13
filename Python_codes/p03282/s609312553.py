S = list(input())
K = int(input())
N = len(S)
ans = 1
for i in range(K):
  if S[i] != '1':
    ans = S[i]
    print(ans)
    break
  elif i == K-1:
    ans = S[i]
    print(ans)
    break