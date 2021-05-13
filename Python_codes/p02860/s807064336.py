N = int(input())
S = input()

A = S[:N//2]
B = S[N//2:]

if A==B:
  print("Yes")
else:
  print("No")