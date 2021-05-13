n = int(input())
b = list(map(int, input().split()))
a = [b[0], b[0]]
c = b[0]
d = b[0]
for i in range(1, n - 1):
  if b[i] >= a[i]:
    a.append(b[i])
  else:
    a[i] = b[i]
    a.append(b[i])
print(sum(a))