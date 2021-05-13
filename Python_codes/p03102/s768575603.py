N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
t = 0
def judge(x):
  s = 0
  for i in range(M):
    s += B[i]*x[i]
  s += C
  if s>0:
    return 1
  else:
    return 0
for a in A:
  t = t + judge(a)
print(t)