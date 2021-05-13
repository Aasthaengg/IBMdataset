import sys
readline = sys.stdin.readline

Q = int(readline())

# 10 ** 5までの「2017に似た数」を全て求めておく

fact = [True] * (10 ** 5 + 1)
fact[0] = False
fact[1] = False
like2017 = [0] * (10 ** 5 + 1)
for i in range(2, len(fact)):
  if fact[i]:
    if i % 2 == 1 and fact[(i + 1) // 2]:
      like2017[i] = 1
    for j in range(i * 2, len(fact), i):
      fact[j] = False
        
for i in range(1, len(like2017)):
  like2017[i] += like2017[i - 1]

for i in range(Q):
  l,r = map(int,readline().split())
  print(like2017[r] - like2017[l - 1])
