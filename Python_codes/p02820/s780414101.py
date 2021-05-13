N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
li = [[] for _ in range(K)]
for k in range(N):
  if T[k] == 'r':
    li[k%K].append([P, 'r'])
  elif T[k] == 's':
    li[k%K].append([R, 's'])
  else:
    li[k%K].append([S, 'p'])
ans = 0
for k in range(K):
  j = 0
  while j < len(li[k])-1:
    if li[k][j][1] == li[k][j+1][1]:
      count = 0
      while(li[k][j+count][1] == li[k][j+count+1][1]):
        count += 1
        if j + count > len(li[k])-2:
          break
      dp = [0, 0]
      for l in range(count+1):
        dp[l%2] += li[k][j+l][0]
        dp[l%2] = max(dp)
      ans += max(dp)
      j += count
    else:
      ans += li[k][j][0]
    j += 1
  if j == len(li[k]) - 1:
    ans += li[k][-1][0]
print(ans)
