N = int(input())
A = list(map(int, input().split()))

counter = 0

for i, A_i in enumerate(A):
  if A[A[i]-1] == i + 1 :
    counter += 1
  
print(int(counter/2))