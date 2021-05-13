S = input()
N = len(S)
w = "keyence"
for i in range(7):
  if S[:i] == w[:i] and S[N-7+i:] == w[i:]:
    print("YES")
    break
  elif i == 6:
    print("NO")
