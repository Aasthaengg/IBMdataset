import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
S = readline().rstrip()

unhappy = 0
for i in range(len(S)):
  if i == 0:
    if S[i] == "L":
      unhappy += 1
    if S[i] == "R" and S[i + 1] == "L":
      unhappy += 1
  elif i == len(S) - 1:
    if S[i] == "R":
      unhappy += 1
    if S[i] == "L" and S[i - 1] == "R":
      unhappy += 1
  else:
    if S[i] == "L" and S[i - 1] != "L":
      unhappy += 1
    if S[i] == "R" and S[i + 1] != "R":
      unhappy += 1
      
print(min(N - 1,N - max(unhappy - K * 2,0)))