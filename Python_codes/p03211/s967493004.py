S = input()
ans = 1000
for i in range(len(S)-2):
  s = 100*int(S[i]) + 10*int(S[i+1]) + int(S[i+2])
  ans = min(max(753-s, s-753), ans)
print(ans)