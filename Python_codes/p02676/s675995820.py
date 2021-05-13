K = int(input())
S = input()
 
if len(S) <= K:
  print(S)
elif len(S) > K:
  print(S[0:K]+"...")