a = [int(input()) for i in range(2)]
N = a[0]

s = 1
K = a[1]
for i in range(N):
  if (s+K < 2*s):
    s += K
  else:
    s = s*2

print(s)