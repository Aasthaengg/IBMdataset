S = input()
K = int(input())

if len(S)>=K and S[:K] == "1"*K:
  print("1")
else:
  S = S.replace("1","")
  print(S[0])