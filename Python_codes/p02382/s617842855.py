n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

d1 = 0
for i in range(n):
    d1 += abs(x[i] - y[i])
print('{:.8f}'.format(d1))

d2 = 0
for i in range(n):
    d2 += abs(x[i] - y[i])**2
print('{:.8f}'.format(d2**(1/2)))

d3 = 0
for i in range(n):
    d3 += abs(x[i] - y[i])**3
print('{:.8f}'.format(d3**(1/3)))

d = []
p = float('inf')
for i in range(n):
    d.append(abs(x[i] - y[i]))
print('{:.8f}'.format(max(d)))
