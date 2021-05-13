S,T = input().split()
N,M = list(map(int, input().split()))
s = input()
if s == S:
  print(N-1, M)
else:
  print(N, M-1)