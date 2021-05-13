N = int(input())
A = list(map(int,input().split()))

ans = 0
smallest = 10 ** 9 + 1
nega = 0
for i in range(len(A)):
  if A[i] < 0:
    nega ^= 1
    A[i] *= -1
  ans += A[i]
  if A[i] < smallest:
    smallest = A[i]
  
if nega:
  ans -= smallest * 2
  
print(ans)