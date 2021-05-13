import sys
N, K = [int(x) for x in input().split()]
H = [int(x) for x in input().split()]
H.sort()
if(N<K):
  print(0)
  sys.exit()
else:
  for i in range(1,K+1):
    H[N-i] = 0
print(sum(H))