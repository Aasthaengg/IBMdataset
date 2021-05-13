import sys
N,K = map(int,input().split())
if K>= N:
  print(0)
  sys.exit()
H = list(map(int,input().split()))
H.sort()
print(sum(H[:N-K]))