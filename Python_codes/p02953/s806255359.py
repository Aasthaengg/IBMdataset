n = int(input())
A = list(map(int, input().split( )))
cnt = 0
for i in range(n-1):
  if A[i] < A[i+1]:
    A[i+1] -= 1
  cnt += max(A[i] - A[i+1],0)
  if cnt >= 1:
    print('No')
    exit()
print('Yes')