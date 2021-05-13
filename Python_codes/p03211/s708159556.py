S = input()
l = []
for i in range(0, len(S)-2):
  n = int(S[i]) * 100 + int(S[i+1]) * 10 + int(S[i+2])
  l.append(abs(753 - n))
print(min(l))