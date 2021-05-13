n=[int(input()) for _ in range(int(input()))]
N1,N2=max(n),sorted(n)[-2]
for i in n:
  if i<N1: print(N1)
  elif i==N1: print(N2)