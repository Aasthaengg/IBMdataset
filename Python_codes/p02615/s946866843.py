n = int(input())
A = sorted(map(int, input().split()), reverse=True)
ans = A[0] + sum(2 * a for a in A[1:n//2])
if n % 2 == 1:
  ans += A[n//2]
print(ans)