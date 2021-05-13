n, *A = map(int, open(0).read().split())

def f(x):
  y = 0
  q, r = divmod(x, 2)
  while r == 0:
    y += 1
    q, r = divmod(q, 2)
  return y

B = [0] * 3
for a in A:
  b = f(a)
  B[0] += b == 0
  B[1] += b == 1
  B[2] += b >= 2
print('Yes' if B[0] + (B[1]!=0) <= B[2]+1 else 'No')