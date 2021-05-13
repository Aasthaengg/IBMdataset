A, B, C = map(int, input().split())
K = int(input())
time = 0
while A >= B:
  B *= 2
  time += 1
while B >= C:
  C *= 2
  time += 1
if time <= K:
  print("Yes")
else:
  print("No")