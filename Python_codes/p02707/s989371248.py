# C management

N = int(input())
A = list(map(int, input().split()))

S = [0] * N
for a in A:
  S[a-1] += 1

for s in S:
  print(s)