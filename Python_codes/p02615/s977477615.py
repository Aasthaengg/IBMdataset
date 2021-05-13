n = int(input())

A = list(map(int, input().split()))

A.sort()
A.reverse()

ans = A[0]

L = [0 for i in range(n-1)]

j = 0
for i in range(n-2):
  if L[j] < 2:
    L[j] += 1
    ans += A[j+1]
  else:
    while L[j] >= 2:
      j += 1
    L[j] += 1
    ans += A[j+1]
print(ans)