n=int(input())
S=sorted([int(input()) for i in range(n)])
if sum(S) % 10 != 0:
  print(sum(S))
else:
  for i in range(n):
    if S[i] % 10 != 0:
      print(sum(S)-S[i])
      break
  else:
    print(0)