S = str(input())
K = int(input())

one = 0

for i in range(len(S)):
  if S[i] == "1":
    one += 1
  else:
    notone = S[i]
    break
#print(one,K,notone)
if one >= K:
  print("1")
else:
  print(notone)