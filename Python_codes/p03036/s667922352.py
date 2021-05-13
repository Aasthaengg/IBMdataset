inputted = list(map(int, input().split()))
r = inputted[0]
D = inputted[1]
x2000 = inputted[2]

x_i_1 = (lambda r, D: lambda xi: r * xi - D)(r, D)


for i in range(1, 10 + 1):
    current = x_i_1(x2000) if i == 1 else x_i_1(prev)
    print(current)
    prev = current
