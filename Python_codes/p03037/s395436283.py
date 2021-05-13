N, M = list(map(lambda n: int(n), input().split(" ")))
L = []
R = []
for i in range(M):
  tmp = input().split(" ")
  L.append(int(tmp[0]))
  R.append(int(tmp[1]))

maxL = max(L)
minR = min(R)

print(max([minR - maxL + 1, 0]))