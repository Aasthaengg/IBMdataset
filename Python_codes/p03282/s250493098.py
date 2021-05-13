S = input()
K = int(input())
P = len(S) + 1
Q = ""
for i in range(len(S)):
  if S[i] != "1":
    P = i + 1
    Q = S[i]
    break
if K < P:
  print(1)
else:
  print(Q)