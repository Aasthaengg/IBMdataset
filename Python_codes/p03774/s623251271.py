N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]

for a, b in AB:
  check, distance = 1, 400000001
  for i, [c, d] in enumerate(CD):
    if distance > abs(a-c) + abs(b-d):
      distance = abs(a-c) + abs(b-d)
      check = i+1
  print(check)