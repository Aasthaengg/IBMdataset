a, b, k = list(map(int, input().split()))
l = []
c = a
if (a > b):
  c = b
for i in range(1, c+1):
  if a % i == 0 and b % i == 0:
    l.append(i)
l.sort()
print(l[-k])
