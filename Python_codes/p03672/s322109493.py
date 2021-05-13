S=list(input())
for i in range(len(S)):
  S = S[:len(S)-2]
  if S[:len(S)//2] == S[len(S)//2:]:
    print(len(S))
    break
