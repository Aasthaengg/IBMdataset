a, b = list(map(int, input().split()))
x = b - a
t = 0
for i in range(x + 1):
    t += i
print(t - b)
