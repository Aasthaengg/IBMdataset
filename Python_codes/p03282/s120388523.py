def solve():
  S = input()
  K = int(input())
  for k in range(K):
    if S[k]!='1':
      return S[k]
  return 1
print(solve())