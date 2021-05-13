a, b, k = map(int, input().split())
ab = [a, b]
turn = 1
for _ in range(k):
  turn = not turn
  if ab[turn] % 2 == 1:
    ab[turn] -= 1
  ab[turn] //= 2
  ab[not turn] += ab[turn]
print(*ab)