n, a, b = map(int, input().split())
L = [int(i) for i in input().split()]

t = 0
for i in range(n-1):
  if (L[i+1] - L[i])*a > b:
    t += b
  else:
    t += (L[i+1] - L[i])*a

print(t)