N, M = map(int, input().split())
a = [int(i) for i in input().split()]

dic = {}
dic[1] = 2
dic[2] = 5
dic[3] = 5
dic[4] = 4
dic[5] = 5
dic[6] = 6
dic[7] = 3
dic[8] = 7
dic[9] = 6

ls = [-1]*8
dp = [-1]*(N+1)
dp[0] = 0
for i in a:
  j = dic[i]
  if ls[j]<i:
    ls[j] = i

tag = []
for i in range(len(ls)):
  if ls[i]!=-1:
    tag += [i]
for i in range(N+1):
  for j in tag:
    if i+j<=N:
      dp[i+j] = max(dp[i]*10+ls[j], dp[i+j])

print(dp[N])
