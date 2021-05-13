N,K=[int(s) for s in input().split()]
A=[int(s) for s in input().split()]
F=[int(s) for s in input().split()]
A.sort()
F.sort(reverse=1)


def success(x):
  suc_sum=0
  for i in range(N):
    a=x//F[i]
    if A[i]>a:
      suc_sum+=A[i]-a
  if suc_sum<=K:
    return True
  else:
    return False

def bisearch():
  bi_max=10**12
  bi_a=0
  bi_b=bi_max
  while bi_b-bi_a>1:
    c=(bi_a+bi_b)//2
    if success(c):
      bi_a,bi_b=[bi_a,c]
    else:
      bi_a,bi_b=[c,bi_b]
  return [bi_a,bi_b]

a,b=bisearch()
if success(a):
  print(a)
else:
  print(b)    