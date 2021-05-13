S=input()
ans=0
S=S[:-1]
while True:
  t=len(S)
  if S[:t//2]==S[t//2:]:
    print(len(S))
    break
  S=S[:-1]
