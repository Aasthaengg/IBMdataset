n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = {}
for i in range(m):
  p, x = map(int, input().split())
  px[i] = [p, x]
time = [sum(t)] * m
for i in range(len(px)):
  time[i] = time[i] - t[px[i][0] - 1] + px[i][1]
for e in time:
  print(e)