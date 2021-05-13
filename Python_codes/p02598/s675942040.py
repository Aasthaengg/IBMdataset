# 解答
N, K  = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

def check(L):
  count = 0
  for a in A:
    if a <= L:
      break      
    count += (a-1)//L
    if count > K:
      return False

  return True

l = 0
r = A[0]

while r-l > 1:
  c = (r+l)//2
  if check(c):
    r = c
  else:
    l = c
print(r)