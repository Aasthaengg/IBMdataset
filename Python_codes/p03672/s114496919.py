S = input().strip()
while len(S) > 0:
  S = S[:-1]
  mid = len(S)//2
  if S[:mid] == S[mid:]:
    print(len(S))
    break
  
