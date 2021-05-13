K = int(input())
S = input()

length = len(S)

if length <= K:
  print(S)
  
else:
  S = S[:K]
  print(S + "...")
  
