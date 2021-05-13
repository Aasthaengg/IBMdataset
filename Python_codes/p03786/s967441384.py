N = int(input())
A = list(map(int,input().split()))
A.sort()
cum = [0]*(N)
now = 0
for i in range(N):
  now += A[i]
  cum[i] = now
ans = 0
for i in range(1,N):
  if 2*cum[i-1] < A[i]:
    ans = i
print(N-ans)