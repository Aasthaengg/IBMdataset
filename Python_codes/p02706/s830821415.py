N,M = (int(x) for x in input().split())

hw = [int(x) for x in input().split()]

hwsum = 0

for n in range(len(hw)):
  hwsum += hw[n]

if hwsum<=N:
  print(N-hwsum)
else:
  print(-1)
