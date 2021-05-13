# B Count Balls

N, A, B = map(int, input().split())

set, mod = divmod(N, (A + B))
ans = set * A

if mod < A:
  ans += mod
else:
  ans += A

print(ans)