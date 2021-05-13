def binary_search(A, target):
  left = 0 
  right = len(A)
  while(3 <= right - left):
    index = (left + right) // 2
    if(A[index] < target):
      left = index
    else:
      right = index + 1
  return left
  
N = int(input())
A = list(map(int, input().split()))
A.sort()
target = A[N - 1] / 2
if(target <= A[0]): ai = A[0]
elif(A[N - 2] <= target): ai = A[N - 2]
else:
  index = binary_search(A[:N - 1], target)
  ai = A[index] if(abs(A[index] - target) < abs(A[index + 1] - target)) else A[index + 1]
print(A[N - 1], ai)