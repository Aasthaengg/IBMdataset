K = int(input())
S = input()
sentence=""
if len(S) <= K:
  print(S)
  exit(0)
if K < len(S):
  for i in range(K):
     sentence = sentence + S[i]
print(sentence + "...")
