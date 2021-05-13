S = input()
l = []
x = 753

for i in range(len(S)-2):
  tmp = int(S[i:i+3])
  l.append(abs(tmp - x))
  
print(min(l))