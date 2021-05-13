def calc_blank_minute(H1, M1, H2, M2, K):
  return (H2 * 60) + M2 - (H1 * 60) - M1 - K

H1, M1, H2, M2, K = map(int, input().split())
ans = calc_blank_minute(H1, M1, H2, M2, K)
print(ans)