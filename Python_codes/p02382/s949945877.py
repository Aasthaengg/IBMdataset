import sys
n = int(sys.stdin.readline())
x = [float(i) for i in sys.stdin.readline().split()]
y = [float(i) for i in sys.stdin.readline().split()]
d = [abs(x_i - y_i) for (x_i, y_i) in zip(x, y)]

# p = 1 ~ 3
for p in range(1, 4):
    print(sum([a ** p for a in d]) ** (1/p))

# p = INFINITE
print(max(d))