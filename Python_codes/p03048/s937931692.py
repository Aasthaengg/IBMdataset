R, G, B, N = [int(i) for i in input().split()]

cnt = 0
for r in range(0, N // R + 1):
  for g in range(0, (N - r * R) // G + 1):
    rest = N - (r * R + g * G)
    if rest >= 0 and rest % B == 0:
      cnt += 1

print(cnt)