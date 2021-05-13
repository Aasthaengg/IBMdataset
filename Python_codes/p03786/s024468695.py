N = int(input())
A = list(map(int, input().split()))
A.sort()
cum_A = A[:]
for i in range(N-1):
  cum_A[i+1] += cum_A[i]
t = 0
for i in range(N-1, 0, -1):
  if A[i] <= 2 * cum_A[i-1]:
    t = i-1
  else:
    break

print(N-t)