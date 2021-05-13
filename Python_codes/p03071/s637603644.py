A, B = map(int, input().split())

if A == B:
  ans = 2 * A
else:
  ans = max(A, B) * 2 - 1
print(ans)