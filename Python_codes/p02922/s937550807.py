A, B = map(int, input().split())
n = 1
c = 0
while True:
    if n >= B:
        print(c)
        break
    else:
        c += 1
        n += A - 1