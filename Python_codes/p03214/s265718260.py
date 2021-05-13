from statistics import mean
_ = input()
A = [int(i) for i in input().split()]
m = mean(A)

min_d = 100
index = 0
for i in range(len(A)):
  if abs(A[i] - m) < min_d:
    min_d = abs(A[i] - m)
    index = i
print(index)