N = int(input())
T = 0
M = {}
for i in range(N):
  s, st = input().split()
  t = int(st)
  T += t
  M[s] = T
X = input()
r = T-M[X]
print(r)
