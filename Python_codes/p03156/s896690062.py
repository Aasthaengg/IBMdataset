_ = input()
a, b = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]

cnt = {0:0, 1:0, 2:0}

for p in P:
  if p <= a:
    cnt[0] += 1
  elif p <= b:
    cnt[1] += 1
  else:
    cnt[2] += 1

print(min(cnt.values()))