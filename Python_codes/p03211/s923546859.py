S = input()
N = len(S)
ans = float("inf")
for i in range(N-2):
  ans = min(ans, abs(753 - int(S[i:i+3])))

print(ans)