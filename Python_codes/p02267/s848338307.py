n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

C = 0
for t in T:
  for s in S:
    if s == t:
      C += 1
      break
print(C)