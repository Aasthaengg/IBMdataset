r, D, x_2000 = map(int, input().split())

x = [0]*11
x[0] = x_2000

for i in range(10):
    x[i+1] = r * x[i] - D
    print(x[i+1])
