N = int(input())
A = [int(i) for i in input().split()]
for i in range(N):
  A[i] -= i
A.sort()
med = N//2
b = A[med]
ans = 0
for i in range(N):
  ans += abs(A[i]-b)
print(ans)