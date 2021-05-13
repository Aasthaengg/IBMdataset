S = list(input())

ans = 1000
L = len(S)
for i in range(L):
  if L - 1 < i + 2:
    break
  
  s = int("".join(S[i:i+3]))
  ans = min(ans,abs(753-s))

print(ans)
