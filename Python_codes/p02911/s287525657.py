N, K, Q = list(map(lambda n: int(n), input().split(" ")))
point = [K - Q] * N
for i in range(Q):
  c = int(input())
  point[c - 1] += 1

print("\n".join(["Yes" if p > 0 else "No" for p in point]))