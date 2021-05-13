from collections import Counter
N = int(input())
A = list(map(int, input().split()))
ca = Counter(A)
ca = sorted(ca.items(), key=lambda x:-x[0])
cnt = 0
m = []
for k, v in ca:
  if 3 >= v >= 2:
    cnt += 1
    m += [k]
  elif v >= 4:
    cnt += 2
    m += [k, k]
  if cnt >= 2:
    break

if len(m) <= 1:
  print(0)
  exit()
print(m[0]*m[1])