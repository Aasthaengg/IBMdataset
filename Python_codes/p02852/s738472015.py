N, M = map(int, input().split())
S = "x" + input()[::-1]
#print("S:", S)

current = 1
masu = [1]

while 1:
  flag = 1
  for i in range(min(current + M, N + 1), current, -1):
    if S[i] == "0":
      flag = 0
      masu.append(i)
      current = i
      break
  if flag:
    print(-1)
    exit()
  if current == N + 1:
    masu = masu[::-1]
    #print("masu:", masu)
    answer = []
    for i in range(1, len(masu)):
      answer.append(- masu[i] + masu[i - 1])
    print(*answer)
    exit()