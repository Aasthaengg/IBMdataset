S = list(input())
T = list(input())
ans = float("inf")
for i in range(len(S)-len(T)+1):
  n = 0
  for j in range(len(T)):
    if T[j] != S[i+j]:
      n += 1
  ans = min(ans,n)
print(ans)