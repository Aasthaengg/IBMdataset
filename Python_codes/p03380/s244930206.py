n = int(input())
a = list(map(int, input().split()))
a.sort()
M = a[-1]
m = a[0]
C = -1
for i in range(n):
  c = a[i]*(M-a[i])
  if C < c:
    C = c
    m = a[i]
  else:
    break
print(M, m, sep=' ')