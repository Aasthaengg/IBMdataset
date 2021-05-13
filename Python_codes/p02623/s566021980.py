def getIntList(strList):
  return list(map(lambda x: int(x), strList))

N, M, K = getIntList(input().split(" "))
A = getIntList(input().split(" "))
B = getIntList(input().split(" "))

ta = 0
tb = 0
TA = [0]
TB = [0]

for i in range(len(A)):
  ta += A[i]
  if ta <= K:
    TA.append(ta)
  else:
    break
for j in range(len(B)):
  tb += B[j]
  if tb <= K:
    TB.append(tb)
  else:
    break

Cij = [0]

j = len(TB) - 1
for i in range(len(TA)):
  while TA[i] + TB[j] > K:
    j += -1
  else:
    if j >= 0:
      Cij.append(i + j)
  if j == -1:
    break


print(max(Cij))
