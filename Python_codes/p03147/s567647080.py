N = int(input())
H = list(map(lambda h: int(h), input().split(" ")))

def f(A):
  if len(A) == 0:
    return 0
  elif len(A) == 1:
    return A[0]
  elif len(A) == 2:
    return max(A)

  c = 0
  if A.count(0) == 0:
    c += min(A)
    A = [a - min(A) for a in A]

  B = split_list(A)
  ret = []
  for j in range(len(B)):
    ret.append(f(B[j]))

  return c + sum(ret)

def split_list(A):
  B = []
  tmp = []
  for i in range(len(A)):
    if A[i] != 0:
      tmp.append(A[i])
    else:
      if len(tmp) > 0:
        B.append(tmp)
        tmp = []
  else:
    if len(tmp) > 0:
      B.append(tmp)
  return B

print(f(H))
