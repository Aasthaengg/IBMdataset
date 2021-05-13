N = int(input())
A = []
for i in range(N):
  A.append(sorted(input()))
A.sort()
ans = 0
c = 1
for i in range(N-1):
  if A[i] == A[i+1]:
    c += 1
  else:
    ans += c * (c-1) // 2
    c = 1
ans += c * (c-1) // 2
print(ans)