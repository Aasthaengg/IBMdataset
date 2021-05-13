N = int(input())
A = list(map(int, input().split()))
dif = 0
sum = 0

for i in range(N - 1):
  if A[i] > A[i + 1]:
    dif = A[i] - A[i + 1]
    sum += dif
    A[i +1] = A[i + 1] + dif
    
print(sum)
