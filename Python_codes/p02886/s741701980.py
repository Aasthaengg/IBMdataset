N = int(input())
A=[int(x) for x in input().split(' ')]

heal = 0

for i in range(N-1):
  for j in range(i+1,N):
    heal += A[i]*A[j]

print(heal)