N = int(input())
A = list(map(int, input().split()))

result = 0
max_len = A[0]
for i in range(1, N):
  if max_len > A[i]:
    result += max_len - A[i]
  else:
    max_len = A[i]
    
print(result)