# A - Connection and Disconnection
# https://atcoder.jp/contests/agc039/tasks/agc039_a

S = list(input())
k = int(input())

S_cnt = 0
repS = S[:]
for i in range(1, len(S)):
  if repS[i] == repS[i - 1]:
    repS[i] = "*"
    S_cnt += 1

if all(i == j for i, j in zip(S, S[1:])):
  ans = len(S) * k // 2
else:
  if S[0] != S[-1]:
    ans = S_cnt * k
  else:
    l = 0
    for s in S:
      if s == S[0]:
        l += 1
      else:
        break
    r = 0
    for s in S[::-1]:
      if s == S[-1]:
        r += 1
      else:
        break
    ans = S_cnt * k - (l // 2 + r // 2 - (l + r) // 2) * (k - 1)

print(ans)