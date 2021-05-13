S =input()
K = int(input())
if S.count("1") == len(S):
  print(1)
else:
  for i in range(len(S)):
    if S[i] != "1":
      print(S[i])
      break
    elif i+1 == K:
      print(S[i])
      break