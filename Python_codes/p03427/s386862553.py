N = int(input())
N = list(str(N))
for i in range(len(N)):
  N[i] = int(N[i])
if len(N) > 1:
  print(max(N[0]-1 + 9*(len(N)-1),sum(N)))
else:
  print(N[0])