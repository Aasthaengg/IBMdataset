N = int(input())
K = int(input())
X = int(input())
Y = int(input())
m =0
if N < K:
  m = N*X
else:
  m = K*X + (N-K)*Y

print(m)