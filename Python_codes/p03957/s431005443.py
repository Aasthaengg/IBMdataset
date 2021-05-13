S = input()
start = -1
next = 0
for i in range(len(S)):
  if S[i] == 'C':
    start = i
    break
if start == -1:
  print('No')
  exit()
if 'F' in S[start:]:
  print('Yes')
  exit()
print('No')