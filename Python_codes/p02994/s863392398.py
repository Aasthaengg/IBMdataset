n, L = map(int, input().split())
l = [0] * n
for i in range(n):
  l[i] = L + i
mins = 10 ** 10
for i in l:
  if abs(mins) > abs(i):
    mins = i
print(sum(l) - mins)