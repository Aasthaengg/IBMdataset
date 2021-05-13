N = int(input())
A = [0] + list(map(int,input().split())) + [0]
pay = [0]*(N+1)
for i in range(N+1):
  pay[i] = abs(A[i] - A[i+1])

sum_pay = sum(pay)
for j in range(1,N+1):
  print(sum_pay + (abs(A[j-1] - A[j+1]) - abs(A[j-1] - A[j]) - abs(A[j] - A[j+1])))