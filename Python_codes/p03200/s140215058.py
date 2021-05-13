S = input()
N = len(S)

W = []
for i in range(N):
  if S[i] == "W":
    W.append(i)

cnt = 0
for i in range(len(W)):
  cnt += W[i] - i
  
print(cnt)  