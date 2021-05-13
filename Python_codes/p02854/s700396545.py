N = int(input())
A = list(map(int, input().split()))
s = sum(A)
c = 0
d = 10000000000000000
a = 0
for i in range(N):
  c += 2*A[i]
  if abs(c - s) < d:
    a = i
    d = abs(c - s)
a1 = sum(A[:(a+1)])
a2 = sum(A[(a+1):])
ans = abs(a1-a2)
print(ans)