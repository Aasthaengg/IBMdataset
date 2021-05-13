n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

p1 = p2 = p3 = p4 = 0

for i in range(n):
    p1 += abs(x[i] - y[i])
    p2 += abs(x[i] - y[i]) ** 2
    p3 += abs(x[i] - y[i]) ** 3
    p4 = max(p4, abs(x[i] - y[i]))

p2 = p2 ** (1 / 2)
p3 = p3 ** (1 / 3)

print("%f\n%f\n%f\n%f\n" % (p1, p2, p3, p4))

