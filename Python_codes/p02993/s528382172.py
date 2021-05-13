S = input()
n = len(S)
flag = False
for i in range(1, n):
  if S[i] == S[i-1]:
    flag = True
if flag == True:
  print('Bad')
else:
  print('Good')