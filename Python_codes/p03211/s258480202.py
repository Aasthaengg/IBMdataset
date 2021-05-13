S=input()

MIN=10**9
for i in range(len(S)-2):
  tmp = abs(int(S[i:i+3])-753)
  if tmp < MIN:MIN=tmp
print(MIN)