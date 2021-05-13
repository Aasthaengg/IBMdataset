S = input()
T = input()

for i in range(len(S)):
  if T == (S[(i+1):len(S)] + S[0:(i+1)]):
    print('Yes')
    break
else:
  print('No')