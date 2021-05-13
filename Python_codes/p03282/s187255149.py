# ans

S = input()
K = int(input())

if S[0:K].count('1') == K:
  print(1)
  exit()
  
for i in range(K):
  if S[i] != '1':
    print(S[i])
    exit()