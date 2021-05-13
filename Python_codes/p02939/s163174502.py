S = input()
N = len(S)
prev = S[0]
ans = 1
i = 1
while i < N:
  ans += 1
  if len(prev) == 2:
    prev = S[i]
    i += 1
    continue
  if prev == S[i] and i < N-1:
    prev = S[i] + S[i+1]
    i += 2
  elif prev == S[i]:
    ans -= 1
    break
  else:
    prev = S[i]
    i += 1
print(ans)