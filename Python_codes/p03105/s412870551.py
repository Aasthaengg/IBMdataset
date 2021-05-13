a,b,c = map(int, input().split())

n = 0

for i in range(c + 1):
    if n < c and b - a >= 0:
        b = b - a
        n = n + 1
    else:
        print(n)
        break