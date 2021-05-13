n = int(input())
A = list(map(int, input().split()))
A.sort()
sumA = sum(A)

q = int(input())
m = list(map(int, input().split()))

def f(A, s, res):
  if res[0]:
    return
  if s == 0:
    res[0] = True
    return
  for i, a in enumerate(A):
    if a > s:
      break
    f(A[i+1:], s-a, res)

for mi in m:
  res = [False]

  if mi <= sumA:
    f(A, mi, res)

  if res[0]:
    print("yes")
  else:
    print("no")