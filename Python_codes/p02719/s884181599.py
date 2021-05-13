import sys
N, K = [int(x) for x in input().split()]
if(N>K):
  ans = N % K
else:
  ans = N
while True:
  n_ans = abs(ans - K)
  if(ans<n_ans):
    print(ans)
    sys.exit()
  else:
    ans = n_ans