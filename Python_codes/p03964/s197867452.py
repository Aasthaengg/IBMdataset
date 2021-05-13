n = int(input())
x, y = 1, 1

for i in range(n):
    t, a = map(int, input().split())

    l = -(-x // t)
    r = -(-y // a)
    if l > r:
        x = t * l
        y = a * l
    else:
        x = t * r
        y = a * r

    #print(x, y)

print(x + y)