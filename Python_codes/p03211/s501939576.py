S = input ()
N =700
for i in range (len(S)-2):
  n = abs (int(S[i:i+3])-753)
  if n < N:
    N = n
print (N)