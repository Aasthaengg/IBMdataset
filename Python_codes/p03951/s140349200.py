def solve():
  N = int(input())
  S = input()
  T = input()
  for i in range(N):
    if S[i:]==T[:N-i]:
      return N+i
  return N*2
print(solve())