S = input()
K = int(input())

ind = -1
for i in range(len(S)):
  if S[i] == '1':
    ind = i
  else:
    break

if ind == -1:
  print(S[0])
elif ind + 1 >= K:
  print(1)
else:
  print(S[ind+1])
