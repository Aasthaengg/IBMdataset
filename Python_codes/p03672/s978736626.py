S = input()
while True:
  S = S[:-1]
  if len(S)%2==0 and S[:len(S)//2]*2==S:
    print(len(S))
    break