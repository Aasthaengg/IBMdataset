n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
  p, q = [int(j) for j in input().split(' ')]
  a[i] = p+q
  b[i] = p-q

a.sort()
b.sort()
print(max(a[-1] - a[0], b[-1] - b[0]))