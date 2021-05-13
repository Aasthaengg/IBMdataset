S=input()
T=input()
for i in range(len(S)):
  S=S[len(S)-1]+S[:len(S)-1]
  if S==T:
    print("Yes")
    break
else:
  print("No")
