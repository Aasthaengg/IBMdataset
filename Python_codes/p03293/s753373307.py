S = input()
T = input()
N = len(S)
V = ["" for i in range(N)]
for i in range(N):
  for j in range(N):
    V[i] = V[i][:] + S[(i+j)%N]
flg = False
for i in range(N):
  if V[i] == T:
    flg = True
if flg:
  print("Yes")
else:
  print("No")