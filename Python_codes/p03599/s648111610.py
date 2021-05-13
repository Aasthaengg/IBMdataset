A, B, C, D, E, F = map(int, input().split())
ans1 = A
ans2 = 0
for i in range(A, F // 100 + 1):
  if any((i - A * j) % B == 0 for j in range(i // A + 1)):
    x = min(E * i, F - i * 100)
    e = max([C * j + (x - C * j) // D * D for j in range(x // C + 1)])
    if e * ans1 > ans2 * i:
      ans1 = i
      ans2 = e
print(ans1 * 100 + ans2, ans2)
