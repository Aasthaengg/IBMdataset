x = [0] * 2011
r, d, x[2000] = map(int, input().split())

for i in range(2001,2011):
    x[i] = r * x[i-1] - d
    print(x[i])
