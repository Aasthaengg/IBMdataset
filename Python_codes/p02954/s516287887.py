S = list(input())
N = len(S)
num = [0] * N
R = [0]
L = [N - 1]
for i in range(1, N):
  if S[i] == 'R':
    R.append(i)
  if S[i] == 'L':
    for j in R:
      num[j] = i - j
    R = []
    if S[i-1] == 'R':
      num[i] = -1
    else:
      num[i] = num[i-1] - 1

ans = [0] * N
for i, val in enumerate(num):
  temp = -(val % 2)
  if val < 0:
    temp = - temp
  ans[i + val + temp] += 1

for i in ans:
  print(i,end=" ")
