def solve():
  ans = 0
  S = input()
  n = len(S)
  for i in range(n//2-1,0,-1):
    if S[:i]==S[i:2*i]:
      return i*2
print(solve())