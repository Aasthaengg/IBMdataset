n = input()
minv = input()
maxv = -1 * 10**9

for j in range(n-1):
  v = input()
  if maxv < v - minv:
    maxv = v - minv
  if minv > v:
    minv = v

print maxv