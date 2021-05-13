N = input()
K = len(N)
c = N[0]
a = 0
for i in range(1,K):
  if N[i] != "9":
    a = 1
if a == 0:
  print(int(c) + 9*(K-1))
else:
  print(int(c) + 9*(K-1)-1)
  

