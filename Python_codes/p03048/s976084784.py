R, G, B, N = map(int, input().split())

cnt = 0
for r in range(0, N + 1):
  for g in range(0, N + 1):
    tmp_N = r * R + g * G
    if tmp_N > N:
      continue
    if (N - tmp_N) % B == 0:
      cnt += 1
print(cnt)
