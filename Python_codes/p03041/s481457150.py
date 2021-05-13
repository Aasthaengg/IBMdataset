N, K = map(int, input().split())
S = str(input())

if S[K-1] == "A":
  print(S[:K-1]+"a"+S[K:])
elif S[K-1] == "B":
  print(S[:K-1]+"b"+S[K:])
else:
  print(S[:K-1]+"c"+S[K:])