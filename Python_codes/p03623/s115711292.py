N = input().split()
x, a, b = int(N[0]), int(N[1]), int(N[2])
s = abs(x - a)
t = abs(x - b)
if s > t:
    print('B')
else:
    print('A')