from sys import exit
S = input()
for i in range(len(S)):
  for j in range(i):
    if S[i] == S[j]:
      print('no')
      exit(0)
  for j in range(i+1,len(S)):
    if S[i] == S[j]:
      print('no')
      exit(0)
print('yes')