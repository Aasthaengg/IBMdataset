S = input()
ans = 10**10
for i in range(len(S)-2):
  n = int(S[i:i+3])
  ans = min(ans, abs(n-753))
print(ans)