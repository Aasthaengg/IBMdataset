S = input()
T = input()
N = len(S)
SD = {}
TD = {}
SN = [0]*N
TN = [0]*N
count = 1
for i in range(N):
  s = S[i]
  if s not in SD:
    SD[s] = count
    count+=1
  SN[i] = SD[s]
count = 1
for i in range(N):
  t = T[i]
  if t not in TD:
    TD[t] = count
    count+=1
  TN[i] = TD[t]
ans = "Yes"
for i in range(N):
  if SN[i]!=TN[i]:
    ans = "No"
    break
print(ans)