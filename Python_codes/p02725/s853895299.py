k, n = map(int, input().split())
lst = [int(i) for i in input().split()]

max_l = 0
for i in range(n):
  if i != n - 1:
    l = lst[i + 1] - lst[i]
  else:
    l = k + lst[0] - lst[i]
  if l > max_l:
    max_l = l
print(k - max_l)