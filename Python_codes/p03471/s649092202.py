# coding: utf-8
# Your code here!

n, y = map(int, input().split())

for yukichi in range(n + 1):
  for higuchi in range(n + 1 - yukichi):
    noguchi = n - yukichi - higuchi
    if (yukichi * 10000 + higuchi * 5000 + noguchi * 1000) == y:
      print(yukichi, higuchi, noguchi)
      exit()
print(-1, -1, -1)