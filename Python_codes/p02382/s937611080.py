n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

p1 = 0
p2b = 0
p3b = 0
pn = 0
for i in range(n):
  p1 += abs(x[i] - y[i])
  p2b += abs((x[i] - y[i]) ** 2)
  p3b += abs(((x[i] - y[i]) ** 3))

p2 = p2b ** 0.5
p3 = p3b ** (1 / 3)
pn = max([abs(x[i] - y[i]) for i in range(n)])

print("{:.10f}".format(p1)) 
print(p2)
print(p3)
print("{:.10f}".format(pn))
