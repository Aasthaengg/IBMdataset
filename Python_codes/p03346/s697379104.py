import sys
input = sys.stdin.readline
n = int(input())
memo = [0 for i in range(n)]
for i in range(n):
  memo[int(input())-1] = i
cand = 0
tmp = 0
for n1, n2 in zip(memo[:], memo[1:]):
  if n2 > n1:
    tmp += 1
    if tmp > cand:
      cand = tmp
  else:
    tmp = 0
print(n - cand - 1)
