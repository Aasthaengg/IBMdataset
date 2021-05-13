S=input()
while True:
  S=S[:-1]
  if len(S)%2==0:
    M=len(S)//2
    if S[:M]==S[M:]:
      break
print(len(S))