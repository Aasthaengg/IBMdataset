S = input()
ans = 0
for i in range(3):
  if S[i] == S[i+1]:
    ans = 1
if ans == 0:
  print('Good')
else:
  print('Bad')