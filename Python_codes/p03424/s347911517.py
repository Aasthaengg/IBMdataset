n = int(input())
S = list(input().split())

L = []
for i in range(len(S)):
  if S[i] not in L:
    L.append(S[i])
if len(L) == 3:
  print("Three")
else:
  print("Four")