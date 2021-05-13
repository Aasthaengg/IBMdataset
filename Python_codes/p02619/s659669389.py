D = int(input())
N = 26
c = [int(i) for i in input().split()]
s = list()
last = [0 for i in range(N)]
score = 0

for i in range(D):
  s.append([int(j) for j in input().split()])

for i in range(D):
  n = int(input())
  last[n-1] = i+1
  for j in range(N):
    last_day = i+1-last[j]
    score -= c[j]*last_day
  score += s[i][n-1]
  print(score)
