S = input()
N = len(S)-1
res = 0

for i in range(2 ** N):
  pw = 0
  for j in range(N):
    if ((i >> j) & 1):
      res += int(S[pw:j+1])
      pw = j+1
  res += int(S[pw:])
  
print(res)