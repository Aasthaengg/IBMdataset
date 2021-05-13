n = int(input())
A = []
ans = 0
for _ in range(n):
  a, b = map(int, input().split())
  ans -= b
  A.append(a+b)
A.sort(reverse=True)
ans += sum(A[::2])
print(ans)