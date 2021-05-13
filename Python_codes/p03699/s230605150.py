# C - Bugged
# https://atcoder.jp/contests/abc063/tasks/arc075_a

n = int(input())
S = [int(input()) for _ in range(n)]

S.sort()

score = sum(S)

if score % 10 != 0:
  print(score)
else:
  for s in S:
    if s % 10 != 0:
      print(score - s)
      exit()
  print(0) 