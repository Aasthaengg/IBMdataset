N = int(input(' '))
A = input().split(' ')
A = [int(A[i]) for i in range(3*N)]
A = sorted(A, reverse=True)
STG = 0
for i in range(2*N):
  if not i%2==0:
    STG += A[i]
print(STG)