N = int(input())
A = [int(input()) for n in range(N)]
a1 = sorted(A)[-1]
a2 = sorted(A)[-2]

for a in A:
  if a == a1:
    print(a2)
  else:
    print(a1)