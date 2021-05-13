from collections import Counter
N = int(input())
S = list(input())
ans = 10 ** 9
hash = [0] * (N + 1)
memo = 0
for i in range(N):
  if S[i] == "#":
    memo += 1
  hash[i + 1] = memo
dot = [0] * (N + 1)
memo = 0
for i in range(N - 1,-1,-1):
  if S[i] == ".":
    memo += 1
  dot[i] = memo    
for i in range(N + 1):
  ans = min(ans, hash[i] + dot[i])
print(ans)  