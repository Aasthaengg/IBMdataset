n = int(input())
arr = sorted(list(map(int, input().split())))

m = arr[0]
M = arr[-1]
S = []
for a in arr[1:-1]:
  if a > 0:
    S.append(str(m) + ' ' + str(a))
    m -= a
  else:
    S.append(str(M) + ' ' + str(a))
    M -= a
S.append(str(M) + ' ' + str(m))
print(M-m)
[print(s) for s in S]

