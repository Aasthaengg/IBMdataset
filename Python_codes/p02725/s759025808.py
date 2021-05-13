k, n = [int(i) for i in input().split()]
a = sorted([int(i) for i in input().split()])
max_l = a[0] + k - a[-1]
for i in range(n-1):
  if a[i+1] - a[i] >= max_l:
    max_l = a[i+1] - a[i]
print(k - max_l)