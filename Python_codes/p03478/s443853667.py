N, A, B = input().split(' ')
N = int(N)
A = int(A)
B = int(B)
Num = []
Num = list(range(1, N+1))
checkbox = [0]
all = []
for i in range(N):
  cn = str(Num[i])
  for j in range(len(cn)):
    cnk = int(cn[j])
    checkbox.append(cnk)
  check = sum(checkbox)
  if A<= check <= B:
    all.append(Num[i])
  checkbox = [0]
print(sum(all))
