N = int(input())
As = []
for i in range(N):
  A = int(input())
  As.append(A)
Ass = sorted(As)
for i in range(N):
  if As[i]<Ass[-1]:
    print(Ass[-1])
  else:
    print(Ass[-2])