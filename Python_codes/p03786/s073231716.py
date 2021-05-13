N = int(input())
A = list(map(int, input().split()))

A.sort()
tmp = A[0]
ans = 1
for i in range(1, N):
  if tmp*2 >= A[i]:
    tmp += A[i]
    ans += 1
  else:
    tmp += A[i]
    ans = 1
print(ans)