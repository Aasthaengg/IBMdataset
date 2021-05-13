# vim: set fileencoding=utf-8 :
x, y = map(int, raw_input().split())

if x % y == 0:
    print(-1)
    exit()

n = 1
top = pow(10, 18)

while True:
    t = n * x
    if t >= top:
        print(-1)
        break

    if t % y != 0:
        print(t)
        break

    n += 1
