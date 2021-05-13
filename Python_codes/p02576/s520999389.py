n, x, t = map(int, input().split())

if n % x == 0:
    i = n // x
    print(t * i)
if n % x != 0:
    i = n // x + 1
    print(t * i)