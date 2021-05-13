S = input()
f = 0
for i in range(len(S)-1):
  if S[i] == S[i+1]:
    f = 1
if f == 0:
  print('Good')
else:
  print('Bad')