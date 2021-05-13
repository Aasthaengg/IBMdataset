S = input()
L = len(S)
  
for n in range(L):
  S = S[:-1]
  L = len(S)
  if S[:L//2]==S[L//2:]:
    print(L)
    exit()