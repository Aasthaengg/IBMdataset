S = list(input())
T = list(input())
cnt = 0
for t in range(0,int(len(S))):
  if S[t] != T[t]:
    cnt += 1
print(cnt)