N = []
for i in range(3):
    N.append(input())
N = list(map(int, N))
a, b, h = N[0], N[1], N[2]
s = (a + b) * h / 2
print(int(s))