n = int(input())
minnums = [[] for _ in range(n)]
maxnums = [[] for _ in range(n)]

for i in range(n):
  minnums[i], maxnums[i] = map(int, input().split())
  
minnums.sort()
maxnums.sort()

if n % 2:
  minmedian = minnums[n // 2]
  maxmedian = maxnums[n // 2]
  print(maxmedian - minmedian + 1)
else:
  minmedian = (minnums[n // 2 - 1] + minnums[n // 2]) / 2
  maxmedian = (maxnums[n // 2 - 1] + maxnums[n // 2]) / 2
  print(int((maxmedian - minmedian) * 2 + 1))