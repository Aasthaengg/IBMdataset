N, M = map(int, input().split())
S = list(map(int, list(input())))
S.reverse()

ans = []

i=0
while i < N:
  max = 0
  for j in range(1, M+1):
    if i + j < N+1:
      if S[i+j] == 0:
        max = j
  if max == 0:
    print(-1)
    exit()
  ans.insert(0, max)
  i += max
for i in ans:
  print(i,end=" ")