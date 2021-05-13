r, D, x = map(int, input().split())

for i in range(1, 10+1):
    x = r*x - D
    print(x)
