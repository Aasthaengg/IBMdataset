H1, M1, H2, M2, K = list(map(int, input().strip().split()))
ans = H2 * 60 + M2 - H1 * 60 - M1
if ans <= 0:
  ans += 24 * 60
print(ans - K)