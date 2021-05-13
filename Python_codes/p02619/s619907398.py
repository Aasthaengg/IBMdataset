D = int(input())
C = list(map(int, input().split()))
S = []
for day in range(D):
  S.append(list(map(int, input().split())))
T = []
for day in range(D):
  T.append(int(input()) - 1)
lasts = [-1] * 26
ans = 0
# simulate every day.
for day in range(D):
  ans += S[day][T[day]]
  lasts[T[day]] = day
  # verification for each contests.
  for i in range(26):
      ans -= C[i] * (day - lasts[i])
  print(ans)
