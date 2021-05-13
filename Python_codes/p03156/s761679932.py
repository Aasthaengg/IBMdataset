n = int(input())
a, b = map(int, input().split())
counts = [0] * 3
for q in map(int, input().split()):
  if q <= a:
    counts[0] += 1
  elif a + 1 <= q <= b:
    counts[1] += 1
  else:
    counts[2] += 1

print(min(counts))