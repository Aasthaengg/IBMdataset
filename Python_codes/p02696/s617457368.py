A,B,N=map(int, input().split())

if A == 1: print(0)
elif B == 1: print(0)

else:
  if N ==1: x=1
  elif N < B: x = N
  else:x = B-1
  print(int(A*x/B) - A*int(x/B))