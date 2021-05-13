S = input()
ans = 999

for s in range(len(S)-2):
  ans = min(abs(753-int(S[:3])),ans)
  S = S[1:]
            
print(ans)