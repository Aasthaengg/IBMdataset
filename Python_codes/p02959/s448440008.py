n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = sum(a)

for i in range(n):
  if b[i] > a[i]:
    b[i] -= a[i]
    a[i] = 0
    a[i+1] = max(0, a[i+1]-b[i])
  else:
    a[i] -= b[i]

print(total - sum(a))