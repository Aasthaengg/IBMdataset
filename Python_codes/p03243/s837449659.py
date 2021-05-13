n =  list(input())
N = [int(n[i]) for i in range(len(n))]
if N[0] == max(N):
  print(max(N) * 100 + max(N)*10 + max(N))
else:
  m = N[0]+1
  print(m * 100 + m * 10 + m)
