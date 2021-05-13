N,K = map(int,input().split())
L = [i for i in map(int,input().split())]
res = (N-1)//(K-1)
if (N-1) % (K-1) != 0:
  print(res+1)
else:
  print(res)