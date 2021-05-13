a = input().split()
N = int(a[0])
budget = int(a[1])
b = [int(s) for s in input().split()]
c = sorted(b)
d = int(0)
for i in range(N-1):
  if budget >= c[i]:
    budget = budget - c[i]
    d = d + 1
  else:
    break

if c[N-1] == budget:
    d = d + 1

print(d)