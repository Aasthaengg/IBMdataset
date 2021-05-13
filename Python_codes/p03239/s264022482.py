n, T = map(int, input().split())
arr = []
for i in range(n):
  c, t = map(int, input().split())
  if T >= t:
    arr.append([c,t])
arr.sort()
if len(arr) >= 1:
  print(arr[0][0])
else:
  print('TLE')