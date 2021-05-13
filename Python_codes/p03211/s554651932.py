L = []
S = input()
for i in range(len(S)-2):
  n = int(S[i] + S[i+1] + S[i+2])
  L.append(abs(753-n))
L.sort()
print(L[0])