n, k = map(int, input().split())
hps = sorted(list(map(int, input().split())), reverse=True)
if n <= k:
  print(0)
else:
  print(sum(hps[k:]))