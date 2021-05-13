x = [None]*11

r, d, x[0] = map(int, input().split())

for i in range(10):
    x[i+1] = r*x[i] - d
    print(x[i+1])