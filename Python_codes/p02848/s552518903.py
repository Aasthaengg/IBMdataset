N = int(input())
S = list(input())
for i in range(len(S)):
  if ord(S[i])+N <= 90:
    S[i] = chr(ord(S[i])+N)
  else:
    S[i] = chr(ord(S[i])+N-26)
for j in S:
  print(j,end = "")