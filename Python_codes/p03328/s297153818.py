a, b = map(int, input().split())

s = 0
for i in range(1, 1000):
    s += i
    if i == b - a:
        print(s - b)
        exit